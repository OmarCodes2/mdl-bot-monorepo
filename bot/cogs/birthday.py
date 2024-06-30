import discord
import random
import os
import json
from discord.ext import commands, tasks
from utils import load_key, encrypt_data, decrypt_data
from datetime import datetime, timedelta
import pytz

class Birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.birthday_gifs = self.load_gif_links('birthday_gifs.txt')
        self.encryption_key = load_key()
        self.birthdays = self.load_birthdays()
        self.check_birthdays.start()

    def load_gif_links(self, file_name):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, file_name)
        with open(file_path, "r") as file:
            return [line.strip() for line in file if line.strip()]

    def load_birthdays(self):
        try:
            with open("birthdays.json", "r") as file:
                encrypted_data = file.read()
                decrypted_data = decrypt_data(encrypted_data, self.encryption_key)
                return json.loads(decrypted_data)
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Error loading birthdays: {e}")
            return {}

    def save_birthdays(self):
        data = json.dumps(self.birthdays)
        encrypted_data = encrypt_data(data, self.encryption_key)
        with open("birthdays.json", "w") as file:
            file.write(encrypted_data)

    def get_random_birthday_gif(self):
        return random.choice(self.birthday_gifs)

    @commands.command(name='bday')
    async def set_birthday(self, ctx, date: str, user_id: int):
        self.birthdays[str(user_id)] = date
        self.save_birthdays()
        await ctx.send(f"Birthday for user with ID {user_id} set to {date}")

    @tasks.loop(minutes=1)
    async def check_birthdays(self):
        now = datetime.now(pytz.timezone('America/New_York'))
        current_time = now.strftime("%H:%M")
        if current_time == "09:00":
            today = now.strftime("%m-%d")
            for user_id, bday in self.birthdays.items():
                if bday == today:
                    member = self.bot.get_user(int(user_id))
                    if member:
                        channel = self.bot.get_channel(1256934233146916915)
                        if channel:
                            gif_url = self.get_random_birthday_gif()
                            await channel.send(f"Happy Birthday <@{user_id}>!", embed=self.create_birthday_embed(member, gif_url))
                            confirmation_channel = self.bot.get_channel(1242259751879049336)
                            if confirmation_channel:
                                await confirmation_channel.send(f"Confirmation: Birthday message sent for <@{user_id}>")
    
    def create_birthday_embed(self, member, gif_url):
        embed = discord.Embed(
            title=":tada: Happy Birthday! :tada:",
            description=f"Happy Birthday {member.mention}! 🎉🎂",
            color=discord.Color.blue()
        )
        embed.set_image(url=gif_url)
        return embed

    @check_birthdays.before_loop
    async def before_check_birthdays(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(Birthday(bot))
