import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pytz
from openai import OpenAI

load_dotenv()

bot_token = os.getenv('DISCORD_BOT_TOKEN')
testing_channel_id = os.getenv('BOT_TESTING_CHANNEL_ID')
openai_api_key = os.getenv('OPENAI_API_KEY')

if not bot_token:
    raise ValueError("No DISCORD_BOT_TOKEN found in .env file")
if not testing_channel_id:
    raise ValueError("No BOT_TESTING_CHANNEL_ID found in .env file")
if not openai_api_key:
    raise ValueError("No OPENAI_API_KEY found in .env file")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)
openAIClient = OpenAI()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(int(testing_channel_id))
    if channel:
        await channel.send(f'Deployed and Running')
    else:
        raise ValueError(f"Channel ID {testing_channel_id} not found")

@bot.command(name='summary')
async def summary(ctx):
    all_messages = []
    server_name = ctx.guild.name

    for channel in ctx.guild.text_channels:
        async for message in channel.history(limit=100):
            message_details = (
                f"[In {channel.name} {message.author.display_name} sent this at {message.created_at.isoformat()}: {message.content}]"
            )
            all_messages.append(message_details)
    
    combined_message_text = f"Messages for {server_name}:\n" + " / ".join(all_messages)

    combined_summary = await summarize_messages(combined_message_text)
    
    if combined_summary:
        await ctx.send(f"Summary for all channels:\n{combined_summary}")
    else:
        await ctx.send("No messages to summarize for the past day in any channel.")

async def summarize_messages(messages):
    print(messages)
    response = openAIClient.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Create a summary for every channel mention in the form: Channel name: bullet points:\n\n{messages}"}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print(response)
    summary = response.choices[0].message.content.strip()
    return summary



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('Hello'):
        await message.channel.send('Hello')
    await bot.process_commands(message)

bot.run(bot_token)
