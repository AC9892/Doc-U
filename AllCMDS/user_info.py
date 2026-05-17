import discord
from discord.ext import commands

from .common import docs_embed


class UserInfoCommand(commands.Cog):
    @commands.hybrid_command(name="userinfo", description="Show information about a user or guild member.")
    async def userinfo(self, ctx: commands.Context, member: discord.Member | None = None) -> None:
        target = member or ctx.author
        fields = [
            ("ID", str(target.id)),
            ("Account created", discord.utils.format_dt(target.created_at, style="F")),
        ]
        if isinstance(target, discord.Member):
            fields.extend(
                [
                    ("Joined server", discord.utils.format_dt(target.joined_at, style="F") if target.joined_at else "Unknown"),
                    ("Top role", target.top_role.mention),
                    ("Bot account", str(target.bot)),
                ]
            )
        embed = docs_embed(f"User Info: {target}", "Member data comes from Discord cache and gateway intents.", fields)
        embed.set_thumbnail(url=target.display_avatar.url)
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UserInfoCommand())
