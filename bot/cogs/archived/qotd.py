import discord
from discord.ext import commands, tasks
from datetime import datetime
import pytz
import asyncio

class qotd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.messages = [
            "Whoa @everyone ! 🚨 New members alert! 🚨",
            "Scanning... So many new faces! 👀",
            "Overload! Brain freeze! 🧠❄️",
            "Quick! Turning on QOTD mode to handle the swag!",
            "Warning: Too much coolness detected. QOTW transforming into...",
            "✨ Question of the Day! ✨",
            "Buckle up, everyone! For the next ten days, I'll be grilling you with daily questions! 🔥",
            "Prepare for fun, laughs, and maybe a bit of chaos! 😜",
            "Let's start this party! Today's question is...",
            "Loading..."
            "Loading..."
        ]
        self.message_index = 0
        self.send_messages.start()

    @tasks.loop(minutes=1)
    async def send_messages(self):
        now = datetime.now(pytz.timezone('America/New_York'))
        current_time = now.strftime("%H:%M")
        if current_time == "19:30" and self.message_index == 0:
            channel = self.bot.get_channel(1233797948597342341)
            if channel:
                await self.schedule_messages(channel)

    async def schedule_messages(self, channel):
        for message in self.messages:
            await channel.send(message)
            self.message_index += 1
            await asyncio.sleep(15)

    @send_messages.before_loop
    async def before_send_messages(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(qotd(bot))
