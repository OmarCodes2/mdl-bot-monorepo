import random
import discord
from discord.ext import commands

class Watercooler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.topics = [
            "What's your favorite movie?",
            "If you could travel anywhere, where would you go?",
            "What's the best meal you've ever had?",
            "What's your favorite book?",
            "If you could have any superpower, what would it be?",
            "What's your favorite hobby?",
            "What's the best concert you've ever attended?",
            "What's your favorite season and why?",
            "What's a fun fact about you?",
            "What's your dream job?",
            "What is your favorite TV show binge-watch?",
            "If you could meet any historical figure, who would it be?",
            "What's the most adventurous thing you've ever done?",
            "What's your go-to karaoke song?",
            "What's your favorite quote or saying?",
            "If you could have dinner with any celebrity, who would it be?",
            "What's your favorite childhood memory?",
            "What's the best gift you've ever received?",
            "If you could instantly learn any skill, what would it be?",
            "What's your favorite holiday and why?",
            "What's your favorite place on campus?",
            "What's your favorite way to relax after a long day?",
            "If you could live in any time period, which would it be?",
            "What's your favorite board game or card game?",
            "What's your favorite type of cuisine?",
            "If you could swap lives with anyone for a day, who would it be?",
            "What's your favorite thing about being a student?",
            "What's the most interesting class you've ever taken?",
            "What's your favorite genre of music?",
            "If you could travel back in time, where would you go?",
            "What's your favorite sport to watch or play?",
            "If you could be any animal, which would you be?",
            "What's your favorite dessert?",
            "What's your favorite app on your phone?",
            "What's the best advice you've ever received?",
            "What's your favorite weekend activity?",
            "If you could learn any language, what would it be?",
            "What's your favorite way to stay active?",
            "What's the coolest place you've ever visited?",
            "What's your favorite ice cream flavor?",
            "What's your favorite way to spend a rainy day?",
            "If you could create a new holiday, what would it be?",
            "What's your favorite thing to do with friends?",
            "What's your favorite subject in school?",
            "What's your go-to comfort food?",
            "What's your favorite book or series?",
            "If you could have any job for a day, what would it be?",
            "What's your favorite way to volunteer or give back?",
            "What's the most interesting documentary you've seen?",
            "What's your favorite way to spend a day off?",
            "What's your favorite outdoor activity?",
            "What's your favorite way to unwind?",
            "If you could invent something, what would it be?",
            "What's your favorite form of exercise?",
            "What's the best piece of advice you've ever given?",
            "What's your favorite social media platform?",
            "What's your favorite season and why?",
            "What's your favorite type of art or craft?",
            "If you could visit any planet, which would it be?",
            "What's your favorite video game?",
            "What's your favorite way to stay motivated?",
            "What's your favorite place to study?",
            "What's your favorite type of movie?",
            "What's your favorite thing to cook or bake?",
            "What's your favorite festival or fair?",
            "What's your favorite gadget or tech device?",
            "What's your favorite way to spend a Saturday?",
            "If you could have any animal as a pet, what would it be?",
            "What's your favorite quote from a movie or book?",
            "What's your favorite way to practice self-care?",
            "What's your favorite place to shop?",
            "What's your favorite subject to talk about?",
            "If you could be an expert in anything, what would it be?",
            "What's your favorite thing about your hometown?",
            "What's your favorite way to celebrate a milestone?",
            "What's your favorite way to get around (bike, car, walk, etc.)?",
            "What's your favorite plant or flower?",
            "If you could design your perfect day, what would it look like?",
            "What's your favorite thing about your family?",
            "What's your favorite way to meet new people?",
            "What's your favorite thing to collect?",
            "What's your favorite type of weather?",
            "What's your favorite podcast or radio show?",
            "What's your favorite way to learn new things?",
            "What's your favorite thing to do in the summer?",
            "What's your favorite place to relax on campus?",
            "What's your favorite thing about technology?",
            "What's your favorite mode of transportation?",
            "What's your favorite workout routine?",
            "What's your favorite type of tea or coffee?",
            "What's your favorite thing to do on a snow day?",
            "What's your favorite animal at the zoo?",
            "What's your favorite thing about your best friend?",
            "What's your favorite way to spend time with family?",
            "What's your favorite type of puzzle or brainteaser?",
            "What's your favorite thing to do on a Sunday?",
            "What's your favorite way to celebrate a holiday?",
            "What's your favorite type of sandwich?",
            "What's your favorite way to stay organized?",
            "What's your favorite place to visit in your city?",
            "What's your favorite thing about weekends?",
            "What's your favorite way to show appreciation?",
            "What's your favorite TV show or movie to watch with friends?",
            "What's your favorite thing to do in the winter?",
            "What's your favorite kind of cookie?"
        ]

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
