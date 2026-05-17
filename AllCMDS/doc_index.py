import math

import discord
from discord.ext import commands

from .common import docs_embed
from .doc_catalog import DOC_CATEGORIES


class DocIndexView(discord.ui.View):
    def __init__(self, author_id: int, pages: list[discord.Embed]) -> None:
        super().__init__(timeout=180)
        self.author_id = author_id
        self.pages = pages
        self.current = 0
        self._sync()

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id == self.author_id:
            return True
        await interaction.response.send_message("Only the requester can use these buttons.", ephemeral=True)
        return False

    def _sync(self) -> None:
        self.previous_page.disabled = self.current == 0
        self.next_page.disabled = self.current == len(self.pages) - 1

    async def _show(self, interaction: discord.Interaction, index: int) -> None:
        self.current = max(0, min(index, len(self.pages) - 1))
        self._sync()
        await interaction.response.edit_message(embed=self.pages[self.current], view=self)

    @discord.ui.button(label="Back", style=discord.ButtonStyle.primary)
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self._show(interaction, self.current - 1)

    @discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self._show(interaction, self.current + 1)


class DocIndexCommand(commands.Cog):
    @commands.hybrid_command(name="docindex", description="Show a paginated index of discord.py documentation categories.")
    async def docindex(self, ctx: commands.Context) -> None:
        categories = list(DOC_CATEGORIES.items())
        per_page = 4
        total_pages = max(1, math.ceil(len(categories) / per_page))
        pages = []
        for page in range(total_pages):
            embed = docs_embed(
                "discord.py Documentation Index",
                "Use `/docsearch query:<thing>` or `/apiref topic:<thing>` for details.",
            )
            for key, category in categories[page * per_page : (page + 1) * per_page]:
                topics = ", ".join(f"`{topic}`" for topic in list(category["topics"].keys())[:14])
                embed.add_field(name=f"{category['title']} (`{key}`)", value=f"{category['url']}\n{topics}", inline=False)
            embed.set_footer(text=f"Page {page + 1}/{total_pages}")
            pages.append(embed)

        view = DocIndexView(ctx.author.id, pages)
        if ctx.interaction:
            await ctx.interaction.response.send_message(embed=pages[0], view=view, ephemeral=True)
            return
        await ctx.reply(embed=pages[0], view=view, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DocIndexCommand())
