from discord.ext import commands

from .common import docs_embed
from .doc_catalog import iter_doc_topics


class DocSearchCommand(commands.Cog):
    @commands.hybrid_command(name="docsearch", description="Search the local discord.py documentation catalog.")
    async def docsearch(self, ctx: commands.Context, *, query: str) -> None:
        needle = query.lower().strip()
        matches = [
            topic
            for topic in iter_doc_topics()
            if needle in topic["topic_key"] or needle in topic["name"].lower() or needle in topic["summary"].lower()
        ][:10]

        if not matches:
            embed = docs_embed("No Documentation Matches", f"No local catalog results for `{query}`. Try `/docindex`.")
        else:
            embed = docs_embed("Documentation Search", f"Top local catalog results for `{query}`.")
            for topic in matches:
                embed.add_field(
                    name=f"{topic['name']} (`{topic['topic_key']}`)",
                    value=f"{topic['summary']}\n{topic['url']}",
                    inline=False,
                )

        if ctx.interaction:
            await ctx.interaction.response.send_message(embed=embed, ephemeral=True)
            return
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DocSearchCommand())
