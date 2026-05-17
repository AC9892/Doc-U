from discord.ext import commands

from .common import docs_embed, send_guide


class SlashCommandsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="slashcommands", description="Explain slash commands and interactions.")
    async def slashcommands(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Slash Commands",
            "Slash commands are application commands registered with Discord and invoked through interactions.",
            [
                ("Decorator", "Use `@app_commands.command` for pure slash commands or `@commands.hybrid_command` for slash plus prefix."),
                ("Responses", "Use `interaction.response.send_message`, then `followup.send` after the initial response."),
                ("Syncing", "Global sync can take time to appear. Guild-scoped sync is faster during development."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/interactions/api.html"),
            ],
        )
        await send_guide(ctx, embed, "Example slash command:\n```py\nfrom discord import app_commands\n\n@app_commands.command(name=\"hello\", description=\"Say hello\")\nasync def hello(interaction):\n    await interaction.response.send_message(\"Hello\", ephemeral=True)\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SlashCommandsGuideCommand())
