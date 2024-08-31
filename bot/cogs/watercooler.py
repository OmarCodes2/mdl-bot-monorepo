import os
import random
import discord
from discord.ext import commands, tasks
from datetime import datetime, time, timedelta
import giphy_client
from giphy_client.rest import ApiException
import pytz

class Watercooler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.giphy_api_key = os.getenv('GIPHY_API_KEY')
        if not self.giphy_api_key:
            raise ValueError("No GIPHY_API_KEY found in environment variables")
        self.giphy_instance = giphy_client.DefaultApi()
        self.topics = self.load_topics_from_file("questions.txt")
        self.channel_id = 1233797948597342341  # Change to your channel ID
        self.target_time = time(20, 00, 0)  # Set target time to 8:00 PM
        self.check_time.start()

    def load_topics_from_file(self, file_name):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, file_name)
        with open(file_path, "r") as file:
            topics = [line.strip().split('|') for line in file if line.strip()]
        return topics

    def save_topics_to_file(self, file_name, topics):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, file_name)
        with open(file_path, "w") as file:
            for topic_pair in topics:
                file.write(f"{topic_pair[0]}|{topic_pair[1]}\n")

    @tasks.loop(minutes=1)
    async def check_time(self):
        now = datetime.now(pytz.timezone('America/New_York'))
        if now.weekday() == 0 and now.time() >= self.target_time and (now.time() <= (datetime.combine(now, self.target_time) + timedelta(minutes=1)).time()):
            await self.send_watercooler_question()

    async def send_watercooler_question(self):
        if not self.topics:
            print("No more topics available.")
            return

        topic_pair = self.topics.pop(0)
        question, short_topic = topic_pair[0], topic_pair[1]

        embed = discord.Embed(
            title="Question of the Day",
            description=question.strip(),
            color=discord.Color.blue()
        )

        gif_url = self.get_gif_url(short_topic.strip())
        if gif_url:
            embed.set_image(url=gif_url)
        else:
            embed.set_footer(text="No GIF found for this topic.")

        channel = self.bot.get_channel(self.channel_id)
        if channel:
            await channel.send(embed=embed)

        self.save_topics_to_file("questions.txt", self.topics)

    def get_gif_url(self, query):
        try:
            response = self.giphy_instance.gifs_search_get(
                self.giphy_api_key, query, limit=1
            )
            if response.data:
                return response.data[0].images.fixed_height.url
        except ApiException as e:
            print(f"Exception when calling Giphy API: {e}")
        return None

    @check_time.before_loop
    async def before_check_time(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(Watercooler(bot))
