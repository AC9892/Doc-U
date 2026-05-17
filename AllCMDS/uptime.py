from discord.ext import commands

from .common import human_timedelta


class UptimeCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name="uptime", description="Show how long the bot has been online.")
    async def uptime(self, ctx: commands.Context) -> None:
        await ctx.reply(f"Online for `{human_timedelta(self.bot.start_time)}`.", mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UptimeCommand(bot))
