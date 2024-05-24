import discord
from discord.ext import commands

class Praise(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='praise')
    async def praise(self, ctx, member: discord.Member, *, reason: str):
        try:
            member_avatar_url = member.avatar.url if member.avatar else member.default_avatar.url

            embed = discord.Embed(
                title=":sparkles: PRAISE ALERT :sparkles:",
                description=f"{ctx.author.mention} praises {member.mention}",
                color=discord.Color.green()
            )
            embed.add_field(name="Reason", value=reason, inline=False)
            embed.set_thumbnail(url=member_avatar_url)
            embed.set_footer(text=f"Praised by {ctx.author.display_name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)

            await ctx.send(embed=embed)
            await ctx.message.delete()
        except Exception as e:
            print(f"Error in praise command: {e}")
            await ctx.send("There was an error trying to praise that member. Please try again.")

async def setup(bot):
    await bot.add_cog(Praise(bot))
