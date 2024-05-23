import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('DISCORD_BOT_TOKEN')
testing_channel_id = os.getenv('BOT_TESTING_CHANNEL_ID')

if not bot_token:
    raise ValueError("No DISCORD_BOT_TOKEN found in .env file")
if not testing_channel_id:
    raise ValueError("No BOT_TESTING_CHANNEL_ID found in .env file")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(int(testing_channel_id))
    if channel:
        await channel.send('Deployed and Running')
    else:
        raise ValueError(f"Channel ID {testing_channel_id} not found")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('Hello'):
        await message.channel.send('Hello')
    await bot.process_commands(message)


@bot.event
async def setup_hook():
    await bot.load_extension("cogs.summarization")
    await bot.load_extension("cogs.watercooler")

bot.run(bot_token)
