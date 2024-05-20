import os
import discord
from dotenv import load_dotenv

load_dotenv()

botToken = os.getenv('DISCORD_BOT_TOKEN')
testingChannelID = os.getenv('BOT_TESTING_CHANNEL_ID')

if not botToken:
    raise ValueError("No DISCORD_BOT_TOKEN found in .env file")
    
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(int(testingChannelID))
    if channel:
        await channel.send(f'Logged in as {bot.user}')
    else:
        raise ValueError(f"Channel ID {testingChannelID} not found")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('Hello'):
        await message.channel.send('Hello')

bot.run(botToken)
