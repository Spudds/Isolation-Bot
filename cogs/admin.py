import discord
from discord.ext import commands

import asyncio


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, channel: discord.TextChannel, *, arg):

        ch_id = channel.id
        channel = self.bot.get_channel(ch_id)

        await channel.send(arg)
        await ctx.send(f"Announcement has been sent to <#{ch_id}>.")


def setup(bot):
    bot.add_cog(Admin(bot))
