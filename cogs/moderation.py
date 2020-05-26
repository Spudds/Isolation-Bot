import discord
import asyncio
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        await ctx.guild.kick(user=user, reason=reason)
        await ctx.send(f"{user.name} ({user.id}) has been successfully kicked for {reason}!")

    # TODO more moderation commands


def setup(bot):
    bot.add_cog(Moderation(bot))
