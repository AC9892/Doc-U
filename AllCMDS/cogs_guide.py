from discord.ext import commands

from .common import docs_embed, send_guide


class CogsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="cogs", description="Explain discord.py cogs.")
    async def cogs(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Cogs",
            "A cog is a class that groups related commands, listeners, checks, and state.",
            [
                ("When to use", "Use cogs when a bot grows beyond a few commands or when features need their own setup and cleanup."),
                ("Required shape", "Subclass `commands.Cog`, define command methods, then expose `async def setup(bot)` and call `await bot.add_cog(...)`."),
                ("Useful hooks", "`cog_load`, `cog_unload`, `cog_check`, `cog_command_error`, `cog_before_invoke`, `cog_after_invoke`."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html"),
            ],
        )
        await send_guide(ctx, embed, "Example cog file:\n```py\nfrom discord.ext import commands\n\nclass Utility(commands.Cog):\n    @commands.hybrid_command(name=\"ping\")\n    async def ping(self, ctx):\n        await ctx.reply(\"Pong\")\n\nasync def setup(bot):\n    await bot.add_cog(Utility())\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CogsGuideCommand())
