import discord
from discord import app_commands
from discord.ext import commands

class Skin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
 
    @app_commands.command(name="player_skin", description="Query and download Minecraft player skin")
    @app_commands.describe(username="Enter player ID")
    async def add(self, interaction: discord.Interaction, username: str):
        embed = discord.Embed(title="Download Skin", url=f"https://mineskin.eu/download/{username}", description="", color=0x96d35f)
        embed.set_author(name=username, icon_url=f"https://mineskin.eu/helm/{username}/100.png")
        embed.set_thumbnail(url=f"https://mineskin.eu/armor/body/{username}/100.png")
        embed.add_field(name="", value="Image source: mineskin.eu", inline=True)
        embed.set_footer(text="🥦 Cauly Bot 🥦")
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Skin(bot))
