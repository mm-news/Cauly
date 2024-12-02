import discord
from discord.ext import commands
from discord import app_commands
import requests
from datetime import datetime

BS_API_TOKEN = "Your Brawl Stars API Key"
BASE_URL = "https://api.brawlstars.com/v1"

def get_battlelog(tag):
    url = f"{BASE_URL}/players/%23{tag}/battlelog"
    headers = {
        "Authorization": f"Bearer {BS_API_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 403:
        print("Error 403: Forbidden. Please check your API key and permissions.")
        return None
    else:
        print(f"Error: {response.status_code}")
        return None

class BattleLogCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="battlelog", description="Get the recent battle log of a specific player")
    async def battlelog(self, interaction: discord.Interaction, player_tag: str):
        await interaction.response.defer()
        battle_log = get_battlelog(player_tag)
        
        if battle_log and 'items' in battle_log:
            recent_battles = battle_log['items'][:3]
            embeds = []
            
            for battle in recent_battles:
                embed = self.create_battle_embed(battle)
                embeds.append(embed)
            
            await interaction.followup.send(embeds=embeds)
        else:
            await interaction.followup.send("Unable to retrieve battle log.")

    def create_battle_embed(self, battle):
        battle_time = datetime.strptime(battle['battleTime'], "%Y%m%dT%H%M%S.%fZ")
        formatted_time = battle_time.strftime("%Y-%m-%d %H:%M:%S")
        
        battle_info = battle['battle']
        event_info = battle['event']
        
        battle_mode = battle_info['mode'].capitalize()
        battle_type = battle_info.get('type', '').capitalize()
        map_name = event_info['map']
        
        embed = discord.Embed(
            title=f"{map_name} ({battle_mode}{'-' + battle_type if battle_type else ''})",
            description=f"Mode: {battle_info['mode'].capitalize()}",
            color=0x00ff00 if battle_info['result'] == 'victory' else 0xff0000
        )
        
        embed.add_field(
            name="Result", 
            value=f"{'Victory' if battle_info['result'] == 'victory' else 'Defeat'} ({battle_info.get('trophyChange', 0):+d}🏆)", 
            inline=True
        )
        embed.add_field(name="Time (UTC)", value=formatted_time, inline=True)
        
        if 'starPlayer' in battle_info:
            star_player = battle_info['starPlayer']
            embed.add_field(
                name="Star Player",
                value=f"{star_player['name']}\n{star_player['brawler']['name']} (Lv.{star_player['brawler']['power']} - {star_player['brawler']['trophies']}🏆)",
                inline=False
            )
        
        if 'teams' in battle_info:
            for i, team in enumerate(battle_info['teams'], 1):
                team_info = []
                for player in team:
                    brawler = player['brawler']
                    team_info.append(f"{player['name']} - {brawler['name']} (Lv.{brawler['power']} - {brawler['trophies']}🏆)")
                embed.add_field(name=f"Team {i}", value="\n".join(team_info), inline=False)
        
        return embed

async def setup(bot):
    await bot.add_cog(BattleLogCog(bot))
