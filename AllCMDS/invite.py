import discord
from discord.ext import commands

from .common import docs_embed


class InviteCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name="invite", description="Get the bot invite link.")
    @commands.is_owner()
    async def invite(self, ctx: commands.Context) -> None:
        if self.bot.user is None:
            await ctx.reply("Bot user is not ready yet.", mention_author=False)
            return
        permissions = discord.Permissions(permissions=8866461766385655)
        url = discord.utils.oauth_url(self.bot.user.id, permissions=permissions, scopes=("bot", "applications.commands"))
        embed = docs_embed("Invite Link", "Use this OAuth2 URL to add the bot to a server.", [("Invite", f"[Click here to invite the bot]({url})")])
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(InviteCommand(bot))
