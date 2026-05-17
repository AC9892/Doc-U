from discord.ext import commands

from .common import docs_embed, send_guide


class InteractionsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="interactions", description="Explain Discord interactions.")
    async def interactions(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Interactions",
            "Interactions power slash commands, context menus, buttons, selects, and modals.",
            [
                ("Initial response", "Use `interaction.response.send_message`, `defer`, `edit_message`, or modal responses."),
                ("Followups", "After the first response, send additional messages with `interaction.followup.send`."),
                ("Ephemeral", "Interaction responses can be ephemeral so only the invoking user sees them."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction"),
            ],
        )
        await send_guide(ctx, embed, "Example interaction response:\n```py\nasync def callback(interaction: discord.Interaction):\n    await interaction.response.defer(ephemeral=True)\n    await interaction.followup.send(\"Done\", ephemeral=True)\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(InteractionsGuideCommand())
