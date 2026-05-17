from discord.ext import commands

from .common import docs_embed, send_guide


class ErrorsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="errors", description="Explain command error handling.")
    async def errors(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Error Handling",
            "discord.py raises structured exceptions for command parsing, checks, cooldowns, and callback failures.",
            [
                ("Prefix commands", "Handle errors with `on_command_error`, `Command.error`, or `Cog.cog_command_error`."),
                ("Slash commands", "Handle app command errors with `bot.tree.error` or cog app-command handlers."),
                ("Common errors", "`CommandNotFound`, `MissingRequiredArgument`, `BadArgument`, `MissingPermissions`, `CommandOnCooldown`."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#exceptions"),
            ],
        )
        await send_guide(ctx, embed, "Example error handler:\n```py\n@bot.event\nasync def on_command_error(ctx, error):\n    if isinstance(error, commands.MissingPermissions):\n        await ctx.reply(\"Missing permissions.\")\n        return\n    raise error\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ErrorsGuideCommand())
