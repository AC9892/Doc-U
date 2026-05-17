from discord.ext import commands

from .common import docs_embed, send_guide


class ComponentsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="components", description="Explain buttons, selects, views, and modals.")
    async def components(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Components and UI",
            "`discord.ui` provides interactive buttons, selects, views, and modals.",
            [
                ("Views", "`discord.ui.View` groups components and owns timeout behavior."),
                ("Buttons and selects", "Use decorators or manually add items with callbacks."),
                ("Persistent views", "Views with stable `custom_id` values can survive restarts when registered on startup."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord-ui-kit"),
            ],
        )
        await send_guide(ctx, embed, "Example button view:\n```py\nclass Confirm(discord.ui.View):\n    @discord.ui.button(label=\"Confirm\", style=discord.ButtonStyle.green)\n    async def confirm(self, interaction, button):\n        await interaction.response.send_message(\"Confirmed\", ephemeral=True)\n\nawait ctx.reply(\"Choose:\", view=Confirm())\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ComponentsGuideCommand())
