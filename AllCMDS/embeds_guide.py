from discord.ext import commands

from .common import docs_embed, send_guide


class EmbedsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="embeds", description="Explain Discord embeds.")
    async def embeds(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Embeds",
            "Embeds make rich Discord messages with structured fields and media.",
            [
                ("Core properties", "`title`, `description`, `url`, `color`, `timestamp`."),
                ("Sections", "`set_author`, `add_field`, `set_thumbnail`, `set_image`, `set_footer`."),
                ("Limits", "Discord enforces per-field and total character limits. Keep generated embeds concise."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed"),
            ],
        )
        await send_guide(ctx, embed, "Example embed:\n```py\nembed = discord.Embed(title=\"Status\", description=\"Online\", color=discord.Color.green())\nembed.add_field(name=\"Latency\", value=\"42ms\")\nawait ctx.reply(embed=embed)\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EmbedsGuideCommand())
