import os
import random
import discord
from discord.ext import commands


class Watercooler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.topics = self.load_topics_from_file("questions.txt")

    def load_topics_from_file(self, file_name):

        script_dir = os.path.dirname(__file__)

        file_path = os.path.join(script_dir, file_name)
        with open(file_path, "r") as file:
            topics = [line.strip() for line in file if line.strip()]
        return topics

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
