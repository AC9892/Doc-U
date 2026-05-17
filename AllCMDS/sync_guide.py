from discord.ext import commands

from .common import docs_embed, send_guide


class SyncGuideCommand(commands.Cog):
    @commands.hybrid_command(name="syncguide", description="Explain slash command syncing.")
    async def syncguide(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Command Tree Syncing",
            "Slash commands must be synced to Discord before users can see them.",
            [
                ("Global sync", "`await bot.tree.sync()` updates global commands but can take time to fully propagate."),
                ("Guild sync", "Use guild-specific syncing while testing because it appears much faster."),
                ("This bot", "`Main.py` syncs the command tree in `on_ready` after loading every extension."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.CommandTree.sync"),
            ],
        )
        await send_guide(ctx, embed, "Example sync:\n```py\n@bot.event\nasync def on_ready():\n    synced = await bot.tree.sync()\n    print(f\"Synced {len(synced)} commands\")\n```\nUse guild sync while testing for faster updates.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SyncGuideCommand())
