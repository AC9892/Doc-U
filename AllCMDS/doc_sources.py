from discord.ext import commands

from .common import docs_embed


class DocSourcesCommand(commands.Cog):
    @commands.hybrid_command(name="docsources", description="Show official discord.py documentation source links.")
    async def docsources(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Official discord.py Documentation Sources",
            "Primary links used by this bot's documentation commands.",
            [
                ("Main docs", "https://discordpy.readthedocs.io/en/stable/"),
                ("API reference", "https://discordpy.readthedocs.io/en/stable/api.html"),
                ("commands extension", "https://discordpy.readthedocs.io/en/stable/ext/commands/"),
                ("commands API", "https://discordpy.readthedocs.io/en/stable/ext/commands/api.html"),
                ("Interactions and app commands", "https://discordpy.readthedocs.io/en/stable/interactions/api.html"),
                ("Tasks extension", "https://discordpy.readthedocs.io/en/stable/ext/tasks/"),
                ("FAQ", "https://discordpy.readthedocs.io/en/stable/faq.html"),
            ],
        )
        if ctx.interaction:
            await ctx.interaction.response.send_message(embed=embed, ephemeral=True)
            return
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DocSourcesCommand())
