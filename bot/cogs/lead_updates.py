import discord
from discord.ext import commands, tasks
from datetime import datetime, time, timedelta
import pytz

class LeadUpdates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 1279239205356175361
        self.target_time = time(19, 00, 0)
        self.check_time.start()

    @tasks.loop(minutes=1)
    async def check_time(self):
        now = datetime.now(pytz.timezone('America/New_York'))
        if now.weekday() == 0 and now.time() >= self.target_time and (now.time() <= (datetime.combine(now, self.target_time) + timedelta(minutes=1)).time()):
            await self.send_lead_update_prompt()

    async def send_lead_update_prompt(self):
        channel = self.bot.get_channel(self.channel_id)
        if channel:
            role_mention = "<@&1221216250248822938>"
            
            embed = discord.Embed(
                title="Weekly Update Reminder",
                description=f"{role_mention} Please submit your weekly updates by the end of the day today.",
                color=discord.Color.red()
            )
            embed.set_footer(text="Thank you for your timely updates!")
            
            await channel.send(embed=embed)

    @check_time.before_loop
    async def before_check_time(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(LeadUpdates(bot))
