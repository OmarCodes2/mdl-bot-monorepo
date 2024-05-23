import os
import random
import discord
from discord.ext import commands
from giphy_client.rest import ApiException
import giphy_client

class Watercooler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.giphy_api_key = os.getenv('GIPHY_API_KEY')
        if not self.giphy_api_key:
            raise ValueError("No GIPHY_API_KEY found in environment variables")
        self.giphy_instance = giphy_client.DefaultApi()
        self.topics = self.load_topics_from_file("questions.txt")

    def load_topics_from_file(self, file_name):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, file_name)
        with open(file_path, "r") as file:
            topics = [line.strip().split('|') for line in file if line.strip()]
        return topics

    @commands.command(name='watercooler')
    async def watercooler(self, ctx):
        topic_pair = random.choice(self.topics)
        question, short_topic = topic_pair[0], topic_pair[1]
        embed = discord.Embed(
            title="Question of the Week",
            description=question.strip(),
            color=discord.Color.blue()
        )

        gif_url = self.get_gif_url(short_topic.strip())
        if gif_url:
            embed.set_image(url=gif_url)
        else:
            embed.set_footer(text="No GIF found for this topic.")

        await ctx.send(embed=embed)

    def get_gif_url(self, query):
        try:
            response = self.giphy_instance.gifs_search_get(self.giphy_api_key, query, limit=1)
            if response.data:
                return response.data[0].images.fixed_height.url
        except ApiException as e:
            print(f"Exception when calling Giphy API: {e}")
        return None

async def setup(bot):
    await bot.add_cog(Watercooler(bot))
