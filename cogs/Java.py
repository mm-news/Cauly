import discord
from discord import app_commands
from discord.ext import commands
from mcstatus import JavaServer

class Java(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="javaserver", description="Query the status of a Java server")
    @app_commands.describe(ip="Enter server address")
    async def check_server(self, interaction: discord.Interaction, ip: str):
        await interaction.response.defer()
        try:
            server = JavaServer.lookup(ip)
            status = server.status()
            await interaction.followup.send(f"{ip} is **OPEN**, and **{status.players.online} player(s)** online.")
        except Exception as e:
            await interaction.followup.send(f"Error querying server status: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Java(bot))