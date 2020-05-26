import asyncio
import sys
import traceback
import discord
from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound)

        # ANCHOR might need to get rid of this bit for the reddit command exception
        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        # error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f"{ctx.command} has been disabled!")

        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"I could not find that member. Please try again.")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Error: {error}")

        else:
            raise error

        print('Ignoring exception in command {}:'.format(
            ctx.command), file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
