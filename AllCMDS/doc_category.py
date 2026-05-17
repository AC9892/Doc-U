from discord.ext import commands

from .common import docs_embed
from .doc_catalog import DOC_CATEGORIES


class DocCategoryCommand(commands.Cog):
    @commands.hybrid_command(name="doccategory", description="Show all catalog topics for one documentation category.")
    async def doccategory(self, ctx: commands.Context, category: str) -> None:
        key = category.lower().strip()
        category_data = DOC_CATEGORIES.get(key)
        if category_data is None:
            available = ", ".join(f"`{name}`" for name in sorted(DOC_CATEGORIES))
            embed = docs_embed("Unknown Documentation Category", f"Available categories: {available}")
        else:
            embed = docs_embed(
                category_data["title"],
                f"Official category docs: {category_data['url']}",
            )
            for topic_key, (name, summary, url) in category_data["topics"].items():
                embed.add_field(name=f"{name} (`{topic_key}`)", value=f"{summary}\n{url}", inline=False)

        if ctx.interaction:
            await ctx.interaction.response.send_message(embed=embed, ephemeral=True)
            return
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DocCategoryCommand())
