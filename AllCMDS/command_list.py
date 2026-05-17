from __future__ import annotations

import math

import discord
from discord.ext import commands

from .common import DOCS_URL, random_embed_color


COMMANDS_PER_PAGE = 8


class CommandListView(discord.ui.View):
    def __init__(self, author_id: int, pages: list[discord.Embed]) -> None:
        super().__init__(timeout=180)
        self.author_id = author_id
        self.pages = pages
        self.current_page = 0
        self.add_item(discord.ui.Button(label="discord.py Docs", style=discord.ButtonStyle.link, url=DOCS_URL))
        self._sync_buttons()

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id == self.author_id:
            return True
        await interaction.response.send_message("Only the command requester can use these buttons.", ephemeral=True)
        return False

    def _sync_buttons(self) -> None:
        last_page = len(self.pages) - 1
        self.first_page.disabled = self.current_page == 0
        self.previous_page.disabled = self.current_page == 0
        self.next_page.disabled = self.current_page == last_page
        self.last_page.disabled = self.current_page == last_page

    async def _show_page(self, interaction: discord.Interaction, page_index: int) -> None:
        self.current_page = max(0, min(page_index, len(self.pages) - 1))
        self._sync_buttons()
        await interaction.response.edit_message(embed=self.pages[self.current_page], view=self)

    @discord.ui.button(label="First", style=discord.ButtonStyle.secondary)
    async def first_page(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self._show_page(interaction, 0)

    @discord.ui.button(label="Back", style=discord.ButtonStyle.primary)
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self._show_page(interaction, self.current_page - 1)

    @discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self._show_page(interaction, self.current_page + 1)

    @discord.ui.button(label="Last", style=discord.ButtonStyle.secondary)
    async def last_page(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self._show_page(interaction, len(self.pages) - 1)

    async def on_timeout(self) -> None:
        for item in self.children:
            if isinstance(item, discord.ui.Button) and item.style != discord.ButtonStyle.link:
                item.disabled = True


class CommandListCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def _command_rows(self) -> list[commands.Command]:
        return sorted(
            [command for command in self.bot.commands if not command.hidden],
            key=lambda command: command.qualified_name,
        )

    def _build_pages(self) -> list[discord.Embed]:
        command_rows = self._command_rows()
        total_pages = max(1, math.ceil(len(command_rows) / COMMANDS_PER_PAGE))
        pages: list[discord.Embed] = []

        for page_number in range(total_pages):
            start = page_number * COMMANDS_PER_PAGE
            page_commands = command_rows[start : start + COMMANDS_PER_PAGE]
            embed = discord.Embed(
                title="Command List",
                description=(
                    "Every command currently loaded from the `AllCMDS` folder.\n"
                    f"Official documentation: {DOCS_URL}"
                ),
                color=random_embed_color(),
                timestamp=discord.utils.utcnow(),
            )

            for command in page_commands:
                signature = command.signature.strip()
                usage = f"/{command.qualified_name}"
                prefix_usage = f"-{command.qualified_name}"
                if signature:
                    prefix_usage = f"{prefix_usage} {signature}"
                description = command.description or command.help or "No description provided."
                cog_name = command.cog_name or "No cog"
                embed.add_field(
                    name=f"`{usage}`",
                    value=(
                        f"{description}\n"
                        f"Prefix: `{prefix_usage}`\n"
                        f"Category: `{cog_name}`"
                    ),
                    inline=False,
                )

            embed.set_footer(text=f"Page {page_number + 1}/{total_pages} | {len(command_rows)} commands loaded")
            pages.append(embed)

        return pages

    @commands.hybrid_command(name="cmdlist", aliases=["commands", "commandlist"], description="Show a paginated embedded list of every command.")
    async def cmdlist(self, ctx: commands.Context) -> None:
        pages = self._build_pages()
        view = CommandListView(ctx.author.id, pages)
        if ctx.interaction:
            await ctx.interaction.response.send_message(embed=pages[0], view=view, ephemeral=True)
            return
        await ctx.reply(embed=pages[0], view=view, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CommandListCommand(bot))
