from discord.ext import commands

from .common import GLOSSARY, docs_embed


class GlossaryCommand(commands.Cog):
    @commands.hybrid_command(name="glossary", description="Define common discord.py terms.")
    async def glossary(self, ctx: commands.Context, term: str = "all") -> None:
        key = term.lower().strip()
        if key == "all":
            fields = [(name, meaning) for name, meaning in sorted(GLOSSARY.items())]
            await ctx.reply(embed=docs_embed("discord.py Glossary", "Common terms used by discord.py and Discord.", fields), mention_author=False)
            return
        meaning = GLOSSARY.get(key)
        if meaning is None:
            await ctx.reply(f"Unknown term. Try `/glossary all`.", mention_author=False)
            return
        await ctx.reply(embed=docs_embed(f"Glossary: {key}", meaning), mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GlossaryCommand())
