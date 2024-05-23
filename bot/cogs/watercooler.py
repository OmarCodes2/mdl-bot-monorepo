import random
import discord
from discord.ext import commands

class Watercooler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.topics = [
            "What's your favorite movie?",
            "If you could travel anywhere, where would you go?",
            "What's the best meal you've ever had?",
            "What's your favorite book?",
            "If you could have any superpower, what would it be?",
            "What's your favorite hobby?",
            "What's the best concert you've ever attended?",
            "What's your favorite season and why?",
            "What's a fun fact about you?",
            "What's your dream job?"
        ]

    @commands.command(name='watercooler')
    async def watercooler(self, ctx):
        topic = random.choice(self.topics)
        embed = discord.Embed(
            title="Watercooler Topic",
            description=topic,
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Watercooler(bot))
