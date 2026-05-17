from discord.ext import commands

from .common import docs_embed
from .doc_catalog import find_doc_topic


class ApiRefCommand(commands.Cog):
    @commands.hybrid_command(name="apiref", description="Show an exact discord.py API reference entry.")
    async def apiref(self, ctx: commands.Context, *, topic: str) -> None:
        match = find_doc_topic(topic)
        if match is None:
            embed = docs_embed("API Reference Not Found", f"No local entry for `{topic}`. Try `/docsearch query:{topic}`.")
        else:
            embed = docs_embed(
                match["name"],
                match["summary"],
                [
                    ("Category", f"{match['category_title']} (`{match['category_key']}`)"),
                    ("Topic key", f"`{match['topic_key']}`"),
                    ("Official docs", match["url"]),
                ],
            )

        if ctx.interaction:
            await ctx.interaction.response.send_message(embed=embed, ephemeral=True)
            return
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ApiRefCommand())
