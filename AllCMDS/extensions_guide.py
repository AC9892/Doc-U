from discord.ext import commands

from .common import docs_embed, send_guide


class ExtensionsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="extensions", description="Explain extension loading.")
    async def extensions(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Extensions",
            "Extensions are Python modules loaded at runtime with `load_extension`.",
            [
                ("Entry point", "Every extension should expose `async def setup(bot): ...`."),
                ("Why they matter", "They make each command or feature reloadable and keep `Main.py` small."),
                ("Common methods", "`load_extension`, `unload_extension`, `reload_extension`."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/ext/commands/extensions.html"),
            ],
        )
        await send_guide(ctx, embed, "Example extension loading:\n```py\n# Main.py\nawait bot.load_extension(\"AllCMDS.ping\")\n\n# AllCMDS/ping.py\nasync def setup(bot):\n    await bot.add_cog(PingCommand(bot))\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExtensionsGuideCommand())
