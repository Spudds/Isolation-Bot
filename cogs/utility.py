import discord
from discord.ext import commands
import asyncio


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! Latency is `{ping}ms` :hourglass:")


def setup(bot):
    bot.add_cog(Utility(bot))
