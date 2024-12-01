import os
import asyncio
import discord
from discord.ext import commands

AUTHORIZED_USER_ID = your_user_id

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Currently logged in as --> {bot.user}")

@bot.command()
async def load(ctx, extension):
    if ctx.author.id == AUTHORIZED_USER_ID:
        await bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == AUTHORIZED_USER_ID:
        await bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == AUTHORIZED_USER_ID:
        await bot.reload_extension(f"cogs.{extension}")
        await ctx.send(f"ReLoaded {extension} done.")


async def load_extensions():
    for filename in os.listdir("./cogs"): # If an error occurs, try using the absolute path
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start("your_token")

if __name__ == "__main__":
    asyncio.run(main())