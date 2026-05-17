from discord.ext import commands

from .common import docs_embed, send_guide


class ConvertersGuideCommand(commands.Cog):
    @commands.hybrid_command(name="converters", description="Explain command converters.")
    async def converters(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Converters",
            "Converters transform command arguments into useful Python objects.",
            [
                ("Built-ins", "`discord.Member`, `discord.User`, `discord.TextChannel`, `discord.Role`, `bool`, `int`, `float`."),
                ("Advanced", "Use `commands.Converter`, `typing.Optional`, `typing.Union`, `Greedy`, and flag converters for complex parsing."),
                ("Slash note", "Slash command options have Discord-native types, so not every prefix converter maps directly."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#converters"),
            ],
        )
        await send_guide(ctx, embed, "Example converter command:\n```py\n@commands.command()\nasync def roleinfo(ctx, role: discord.Role):\n    await ctx.send(f\"Role ID: {role.id}\")\n```\nThe `discord.Role` annotation converts text into a role object.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ConvertersGuideCommand())
