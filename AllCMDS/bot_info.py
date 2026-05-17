import discord
from discord.ext import commands

from .common import docs_embed, human_timedelta


class BotInfoCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name="botinfo", description="Show runtime and library information.")
    async def botinfo(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Bot Information",
            "Runtime details for this discord.py documentation bot.",
            [
                ("discord.py", discord.__version__),
                ("Guilds", str(len(self.bot.guilds))),
                ("Users cached", str(len(self.bot.users))),
                ("Commands loaded", str(len(set(self.bot.commands)))),
                ("Cogs loaded", ", ".join(sorted(self.bot.cogs)) or "None"),
                ("Uptime", human_timedelta(self.bot.start_time)),
                ("GitHub", "[Doc-U Repository](https://github.com/AC9892/Doc-U)"),
                
            ],
        )
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BotInfoCommand(bot))
