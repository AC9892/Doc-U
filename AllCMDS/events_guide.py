from discord.ext import commands

from .common import docs_embed, send_guide


class EventsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="events", description="Explain discord.py events and listeners.")
    async def events(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Events",
            "Events are gateway callbacks such as `on_ready`, `on_message`, `on_member_join`, and `on_interaction`.",
            [
                ("Client events", "Define `@bot.event` functions for global event handlers."),
                ("Cog listeners", "Use `@commands.Cog.listener()` inside cogs for feature-specific listeners."),
                ("Prefix warning", "If you handle `on_message`, call `await bot.process_commands(message)` to keep prefix commands active."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#event-reference"),
            ],
        )
        await send_guide(ctx, embed, "Example event:\n```py\n@bot.event\nasync def on_ready():\n    print(f\"Logged in as {bot.user}\")\n```\nInside cogs, use `@commands.Cog.listener()`.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EventsGuideCommand())
