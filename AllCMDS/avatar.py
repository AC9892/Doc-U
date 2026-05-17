import discord
from discord.ext import commands

from .common import docs_embed


class AvatarCommand(commands.Cog):
    @commands.hybrid_command(name="avatar", description="Show a user's avatar.")
    async def avatar(self, ctx: commands.Context, member: discord.Member | None = None) -> None:
        target = member or ctx.author
        embed = docs_embed(f"Avatar: {target}", "Discord.py exposes avatars as assets with URLs.")
        embed.set_image(url=target.display_avatar.url)
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AvatarCommand())
