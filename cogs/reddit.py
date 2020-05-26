import praw
import prawcore
import json
import asyncio
import discord
from discord.ext import commands
from datetime import datetime

with open("config.json") as config:
    data = json.load(config)

redid = data['reddit-id']
redsecret = data['reddit-secret']
redagent = data['reddit-user-agent']


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    reddit = praw.Reddit(
        client_id=redid, client_secret=redsecret, user_agent=redagent)

    @commands.command()
    async def meme(self, ctx):

        await ctx.trigger_typing()

        submissions = self.reddit.subreddit('memes').random_rising(limit=1)

        embed = discord.Embed(colour=discord.Colour.red())

        for s in submissions:
            try:
                embed.title = "Here's your meme!"
                embed.set_image(url=s.url)
                embed.add_field(
                    name="**Title: **", value=f'**[{s.title}](https://www.reddit.com/{s.permalink})**')
                embed.add_field(
                    name="**Posted by: **", value=f'u/{s.author}')
                embed.set_footer(
                    text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)

            except:
                await ctx.send("Oof, looks like something went wrong. This is usually because of Reddit deciding to die, so try again in a few minutes.")

        await ctx.send(embed=embed)

    @commands.command()
    async def search(self, ctx, query: str, category='hot'):

        try:
            findSub = self.reddit.subreddit(query)
        except commands.CommandInvokeError:
            await ctx.send("error you know what it worked yay")
            return

        if findSub.over18 == True:
            await ctx.send("Subreddits marked as NSFW are a big nono, sorry.")
            return

        if category == 'hot':
            submissions = self.reddit.subreddit(query).hot(limit=5)
        elif category == 'top':
            submissions = self.reddit.subreddit(query).top(limit=5)
        elif category == 'new':
            submissions = self.reddit.subreddit(query).new(limit=5)
        else:
            await ctx.send("Please enter a valid category: Hot, Top, New")
            return

        embed = discord.Embed(colour=discord.Colour.red())

        for s in submissions:
            try:
                embed.title = f"Displaying five {category} posts from r/{query}"
                embed.add_field(name=f"This post has {s.score} upvotes | Posted by {s.author}",
                                value=f'[{s.title}](https://www.reddit.com{s.permalink})', inline=False)

            except:
                await ctx.send("Looks Reddit is unresponsive. Please try again a little later.")
                return

        await ctx.send(embed=embed)

    @search.error
    async def search_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Error: {error}")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"You need to enter a subreddit that you'd like me search!")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("I was unable to find a subreddit with that name. Please try again.")


def setup(bot):
    bot.add_cog(Reddit(bot))
