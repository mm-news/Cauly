import discord
from discord import app_commands
from discord.ext import commands
from mcstatus import BedrockServer

class Bedrock(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
 
    @app_commands.command(name="bedrockserver", description="Query the status of a Bedrock server")
    @app_commands.describe(ip="Enter server address")
    async def add(self, interaction: discord.Interaction, ip: str):
        await interaction.response.defer()
        try:
            server = BedrockServer.lookup(ip)
            status = server.status()
            await interaction.followup.send(f"{ip} is **OPEN**, and **{status.players.online} player(s)** online.")
        except Exception as e:
            await interaction.followup.send(f"Error querying server status: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Bedrock(bot))