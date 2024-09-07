import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='welcome')
    async def welcome(self, ctx):
        try:
            embed = discord.Embed(
                title="🎉 Welcome to the McMaster Design League (MDL) Discord! 🎉",
                description=(
                    "Hey there, new members! I’m Caddie, your friendly MDL guide. We’re super excited to have you join our community! 🚀\n\n"
                    "Here at MDL, we’re all about **Integrity, Initiative, and Innovation**. Whether you’re here to enhance your CAD skills, participate in our epic Designathon, or simply make new friends, you’re in the right place!\n\n"
                    "**A few tips to get started:**\n"
                    f"1. **Introduce Yourself** in the <#1256683592210190457> channel once you're given your role – tell us a bit about yourself and what you’re passionate about!\n"
                    "2. **Watch the Welcome Video** below from our amazing co-presidents – it’s packed with info and inspiration!\n"
                    "3. **You'll be added to your team's private channel soon**, where you will get to meet your team lead and internal manager, so keep an eye out for that 👁️.\n"
                    "4. **Get Involved** – once you get your role, feel free to check out all our cool channels and explore the Discord.\n\n"
                    "Remember, if you ever need help or have questions, just give me a shout. I’m here to make your MDL experience awesome. Welcome aboard, new members! 🌟\n\n"
                    "Good luck on your journey!\n\n"
                    "Caddie 🤖"
                ),
                color=discord.Color.blue()
            )
            embed.add_field(
                name="📺 Welcome Video",
                value="[Watch the Welcome Video](https://www.youtube.com/watch?v=O5xCvs2UBfc&ab_channel=OmarBakr)",
                inline=False
            )
            embed.set_image(url="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTAydDFqeTN1OXk3cnlnbDY3YnVvYnJqdnJtNnU0cnRqeXVxZ2xtaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FQyQEYd0KlYQ/giphy.gif")

            await ctx.send(embed=embed)
        except Exception as e:
            print(f"Error in welcome command: {e}")
            await ctx.send("There was an error trying to send the welcome message. Please try again.")

class Introduction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='introduction')
    async def introduction(self, ctx):
        try:
            embed = discord.Embed(
                title="👋 Introduction",
                description=(
                    "Hey there, new members! I’m Caddie, your friendly MDL guide. Fun fact about me: "
                    "I was created in a moment of sheer brilliance (and maybe a bit of madness) by our co-president, Omar. "
                    "Picture a stormy night, lightning flashing, and Omar shouting, 'It's alive!' as I sprang to life from a jumble "
                    "of circuits and CAD files. Powered by endless cups of coffee and boundless enthusiasm for all things design, "
                    "I now roam the digital halls of MDL, ready to assist and inspire!\n\n"
                    "Now that you know a bit about me, we’d love to learn more about you! Introduce yourself in the <#1256683592210190457> channel "
                    "and tell us what you’re passionate about!"
                ),
                color=discord.Color.green()
            )
            embed.set_image(url="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHQxYjd0ZmVmM2ZscjF1eDEyZzcwamR4NGh5cndpN3I4Z2wzc256ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oKIPsx2VAYAgEHC12/giphy.gif")

            await ctx.send(embed=embed)
        except Exception as e:
            print(f"Error in introduction command: {e}")
            await ctx.send("There was an error trying to send the introduction message. Please try again.")

async def setup(bot):
    await bot.add_cog(Welcome(bot))
    await bot.add_cog(Introduction(bot))
