from discord.ext import commands

from .common import DOC_TOPICS, docs_embed


class DocsCommand(commands.Cog):
    @commands.hybrid_command(name="docs", description="Show a discord.py documentation topic.")
    async def docs(self, ctx: commands.Context, topic: str = "bot") -> None:
        key = topic.lower().strip()
        if key not in DOC_TOPICS:
            available = ", ".join(f"`{name}`" for name in sorted(DOC_TOPICS))
            await ctx.reply(f"Unknown topic. Available topics: {available}", mention_author=False)
            return
        title, summary, url = DOC_TOPICS[key]
        embed = docs_embed(title, summary, [("Reference", url)])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DocsCommand())
