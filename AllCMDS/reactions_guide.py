from discord.ext import commands

from .common import docs_embed, send_guide


class ReactionsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="reactions", description="Explain reactions and raw reaction events.")
    async def reactions(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Reactions",
            "Reactions can be managed from messages and observed through cached or raw reaction events.",
            [
                ("Message APIs", "`Message.add_reaction`, `Message.remove_reaction`, `Message.clear_reactions`."),
                ("Cached events", "`on_reaction_add` needs the message to be cached."),
                ("Raw events", "`on_raw_reaction_add` works even when the message is not cached."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#discord.Reaction"),
            ],
        )
        await send_guide(ctx, embed, "Example reaction:\n```py\nmessage = await ctx.reply(\"Vote now\")\nawait message.add_reaction(\"\\N{THUMBS UP SIGN}\")\n```\nUse raw reaction events when the message might not be cached.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ReactionsGuideCommand())
