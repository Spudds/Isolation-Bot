import discord
from discord.ext import commands

import json
import os
import asyncio

with open("config.json") as config:
    data = json.load(config)

token = data['token']
prefix = data['prefix']

bot = commands.Bot(command_prefix=prefix)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
    print(f"Successfully logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="some sick beats"))


@bot.check
async def block_dms(ctx):
    if ctx.guild is not None:
        return ctx.guild is not None


bot.run(token)
