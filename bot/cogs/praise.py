import discord
from discord.ext import commands

class Praise(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='praise')
    async def praise(self, ctx, *, message: str):
        try:
            members = []
            reason = ""
            words = message.split()
            
            for word in words:
                if word.startswith("<@") and word.endswith(">"):
                    user_id = int(word[2:-1].replace("!", ""))
                    member = ctx.guild.get_member(user_id)
                    if member:
                        members.append(member)
                else:
                    reason += word + " "
            
            reason = reason.strip()

            if not members:
                await ctx.send("You need to mention at least one member to praise.")
                return

            mentions = ", ".join([member.mention for member in members])
            embed = discord.Embed(
                title=":sparkles: PRAISE ALERT :sparkles:",
                description=f"{ctx.author.mention} praises {mentions}",
                color=discord.Color.green()
            )
            embed.add_field(name="Reason", value=reason, inline=False)
            embed.set_footer(text=f"Praised by {ctx.author.display_name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)

            if len(members) == 1:
                member_avatar_url = members[0].avatar.url if members[0].avatar else members[0].default_avatar.url
                embed.set_thumbnail(url=member_avatar_url)
            else:
                embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)

            await ctx.send(embed=embed)
            await ctx.message.delete()
        except Exception as e:
            print(f"Error in praise command: {e}")
            await ctx.send("There was an error trying to praise the members. Please try again.")

async def setup(bot):
    await bot.add_cog(Praise(bot))
