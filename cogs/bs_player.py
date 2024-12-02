import discord
from discord.ext import commands
from discord import app_commands
import requests

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

BS_API_TOKEN = "Your Brawl Stars API Key"
BASE_URL = "https://api.brawlstars.com/v1"

def get_player_info(tag):
    url = f"{BASE_URL}/players/%23{tag}"
    headers = {
        "Authorization": f"Bearer {BS_API_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 403:
        print("Error 403: Forbidden. Please check your API token and permissions.")
        return None
    else:
        print(f"Error: {response.status_code}")
        return None

class BrawlCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="brawlstarts_player", description="Get information about a player")
    async def brawl(self, interaction: discord.Interaction, player_tag: str):
        await interaction.response.defer()
        player_info = get_player_info(player_tag)
        if player_info:
            embed = self.create_embed(player_info)
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send("Unable to obtain player information.")

    def create_embed(self, player_info):
        embed = discord.Embed(
            title=player_info['name'],
            description="Player Data",
            color=0x1ba5f5
        )
        embed.set_thumbnail(url="https://cdn-assets-eu.frontify.com/s3/frontify-enterprise-files-eu/eyJwYXRoIjoic3VwZXJjZWxsXC9maWxlXC82NkFRQW5tVE5EbTNaejN4SDdGZy5wbmcifQ:supercell:aWcyzPsOzXKleie055PH4kkgGtHOMl1DVB5ZyR0Ly48?width=200")
       
        embed.add_field(name="Tag", value=f"{player_info['tag']}", inline=True)
        club_info = player_info.get('club')
        if club_info:
            club_name = club_info['name']
            club_tag = club_info['tag']
            embed.add_field(name="club", value=f"{club_name} ({club_tag})", inline=False)
        
     
        embed.add_field(name="trophies", value=player_info['trophies'], inline=True)
        embed.add_field(name="highestTrophies", value=player_info['highestTrophies'], inline=True)
        
        
        embed.add_field(name="3vs3Victories", value=player_info['3vs3Victories'], inline=True)
        embed.add_field(name="soloVictories", value=player_info.get('soloVictories', 0), inline=True)
        embed.add_field(name="duoVictories", value=player_info.get('duoVictories', 0), inline=True)
        
        return embed

async def setup(bot):
    await bot.add_cog(BrawlCog(bot))