import os
from discord.ext import commands
from openai import OpenAI


openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("No OPENAI_API_KEY found in .env file")

openAIClient = OpenAI(api_key=openai_api_key)


class Summarization(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='summary')
    async def summary(self, ctx):
        all_messages = []
        server_name = ctx.guild.name

        for channel in ctx.guild.text_channels:
            async for message in channel.history(limit=100):
                message_details = (
                    f"[In {channel.name} {message.author.display_name} "
                    f"{message.created_at.isoformat()}: {message.content}]"
                )
                all_messages.append(message_details)

        combined_message_text = (
            f"Messages for {server_name}:\n" + " / ".join(all_messages)
        )
        combined_summary = await self.summarize_messages(combined_message_text)

        if combined_summary:
            await ctx.send(
                f"Summary for all channels:\n{combined_summary}"
            )
        else:
            await ctx.send(
                "No messages to summarize for the past day in any channel."
            )

    async def summarize_messages(self, messages):
        response = openAIClient.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": (
                    "Create a summary for every channel mention in the form: "
                    "Channel name: bullet points:\n\n{messages}"
                )}
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        summary = response.choices[0].message.content.strip()
        return summary


async def setup(bot):
    await bot.add_cog(Summarization(bot))
