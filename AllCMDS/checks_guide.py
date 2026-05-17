from discord.ext import commands

from .common import docs_embed, send_guide


class ChecksGuideCommand(commands.Cog):
    @commands.hybrid_command(name="checks", description="Explain command checks.")
    async def checks(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Checks",
            "Checks stop a command before the callback when a condition is not met.",
            [
                ("Built-ins", "`is_owner`, `has_permissions`, `bot_has_permissions`, `guild_only`, `dm_only`, `cooldown`."),
                ("Custom checks", "Return a predicate from `commands.check(predicate)` for project-specific rules."),
                ("Error handling", "Failed checks raise command errors that can be handled globally or inside a cog."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#checks"),
            ],
        )
        await send_guide(ctx, embed, "Example check:\n```py\n@commands.has_permissions(manage_messages=True)\n@commands.hybrid_command(name=\"purge\")\nasync def purge(self, ctx, amount: int):\n    await ctx.channel.purge(limit=amount)\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ChecksGuideCommand())
