import asyncio
import time
import aiohttp
import random

import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Sends a random cat image.")
    async def cat(self, ctx):
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://aws.random.cat/meow") as r:
                data = await r.json()

                embed = discord.Embed(
                    title="Here's your adorable cat picture!")
                embed.set_image(url=data['file'])
            await ctx.send(embed=embed)

    @commands.command(brief="Sends a random dog image.")
    async def dog(self, ctx):
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://random.dog/woof.json") as r:
                data = await r.json()

                embed = discord.Embed(
                    title="Here's your adorable dog picture!")
                embed.set_image(url=data['url'])
            await ctx.send(embed=embed)

    @commands.command(brief="Sends a random fox image.")
    async def fox(self, ctx):
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as cs:
            async with cs.get("http://randomfox.ca/floof") as r:
                data = await r.json()

                embed = discord.Embed(
                    title="Here's your adorable fox picture!")
                embed.set_image(url=data['image'])
            await ctx.send(embed=embed)

    @commands.command(brief="Sends a random red panda image.")
    async def redpanda(self, ctx):
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/red_panda") as r:
                data = await r.json()

                embed = discord.Embed(
                    title="Here's your adorable red panda picture!")
                embed.set_image(url=data['link'])
            await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, arg):
        if '@' in arg:
            return
        else:
            await ctx.send(arg)

    @commands.command(brief="Starts a fight with someone.")
    async def fight(self, ctx, user: discord.Member):
        fightchoices = [f"{ctx.author.mention} attacks {user.mention} with a plastic foldable chair!",
                        f"{ctx.author.mention} delivers a hefty blow across {user.mention}'s ugly face", f"{ctx.author.mention} pays for the entire US army to mame {user.mention}", f"{user.mention} hides in the Bin to avoid getting attacked", f"{ctx.author.mention} uses a 'shatter resistant' ruler to block {user.mention}'s attack", f"{ctx.author.mention} throws a cat at {user.mention} to momentarily distract them.", f"{user.mention} uses logical reasoning to persuade {ctx.author.mention} to not attacc! What a big brain.", f"{ctx.author.mention} uses some epic magik to create a forcefield. {user.mention} runs away and immediately gets some professional mental help."]

        epicres = random.choice(fightchoices)

        await ctx.send(epicres)

    @commands.command()
    async def howbigbrain(self, ctx, user: discord.Member):
        smartnum = random.randint(1, 100)
        smartnum = str(smartnum)
        await ctx.send(f"{user.mention} is {smartnum}% bigbrain!")

    @commands.command()
    async def howepic(self, ctx, user: discord.Member):
        epicchoices = [f"Sorry, but {user.mention} is definitely more epic than you.",
                       f"Congratulations, {ctx.author.mention}, you are more epic than {user.mention}!"]
        epicres = random.choice(epicchoices)
        await ctx.send(f"{epicres}")

    @commands.command()
    async def randomfact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://uselessfacts.jsph.pl/random.json?language=en") as r:
                data = await r.json()

                fact = data['text']

                await ctx.send(fact)


def setup(bot):
    bot.add_cog(Fun(bot))
