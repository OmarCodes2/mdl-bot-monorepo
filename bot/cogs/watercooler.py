import random
import discord
from discord.ext import commands


class Watercooler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.topics = [
            "Would you rather have dinner with Jay-Z or 500 thousand dollars?",
            "If you could only eat one meal for the rest of your life, what would it be?",
            "What did you want to be when you grew up when you were younger?",
            "Would you rather eat a really good mango or a really good watermelon?",
            "What is the longest you have gone without sleep? (WOOO ENGINEERING!)",
            "Are ghosts real?"
        ]

    @commands.command(name='watercooler')
    async def watercooler(self, ctx):
        topic = random.choice(self.topics)
        embed = discord.Embed(
            title="Question of the Week",
            description=topic,
            color=discord.Color.blue()
        )
        embed.set_image(
            url=(
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGV0c"
                "2pqb3N5aGpuc3U1NHRsNmRkcXJoamxrMThidHRuNjZvODZ3ciZlcD12MV9p"
                "bnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SeysxkSfenHY4/giphy.gif"
            )
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Watercooler(bot))
