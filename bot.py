import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix= "!", intents=discord.Intents.all())

@bot.command
async def on_ready():
    print("woke up!")

@bot.command
async def flood(ctx, channel: discord.TextChannel, times: int, delay: float):
    await ctx.send(f"{channel.name} will receive a total of {times} images.")

    for i in range(times):
        try:
            file_path = "path_your_image.jpg"
            await channel.send(file=discord.File(file_path))
            await ctx.send(f"{i+1}. Image sent to {channel.name} channel.")
        except Exception as e:
            await ctx.send(f"Failed to send image: {e}")
        await asyncio.sleep(delay)

bot.run("YOUR_TOKEN_HERE")