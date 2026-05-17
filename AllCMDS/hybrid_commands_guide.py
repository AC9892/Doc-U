from discord.ext import commands

from .common import docs_embed, send_guide


class HybridCommandsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="hybridcommands", description="Explain hybrid commands.")
    async def hybridcommands(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Hybrid Commands",
            "Hybrid commands expose one callback as both a prefix command and a slash command.",
            [
                ("Decorator", "`@commands.hybrid_command(name=\"example\")`."),
                ("Callback context", "The callback receives `commands.Context`; discord.py bridges interaction data when called as slash."),
                ("Limits", "Slash command option types and names are stricter than prefix command parameters."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#hybrid-commands"),
            ],
        )
        await send_guide(ctx, embed, "Example hybrid command:\n```py\n@commands.hybrid_command(name=\"avatar\")\nasync def avatar(self, ctx, member: discord.Member | None = None):\n    target = member or ctx.author\n    await ctx.reply(target.display_avatar.url)\n```\nUse it as `/avatar` or `-avatar`.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HybridCommandsGuideCommand())
