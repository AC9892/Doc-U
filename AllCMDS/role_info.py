import discord
from discord.ext import commands

from .common import docs_embed


class RoleInfoCommand(commands.Cog):
    @commands.guild_only()
    @commands.hybrid_command(name="roleinfo", description="Show information about a role.")
    async def roleinfo(self, ctx: commands.Context, role: discord.Role) -> None:
        permissions = [name for name, enabled in role.permissions if enabled]
        embed = docs_embed(
            f"Role Info: {role.name}",
            "`discord.Role` stores color, hierarchy position, mentionability, and permission bits.",
            [
                ("ID", str(role.id)),
                ("Created", discord.utils.format_dt(role.created_at, style="F")),
                ("Color", str(role.color)),
                ("Position", str(role.position)),
                ("Mentionable", str(role.mentionable)),
                ("Managed", str(role.managed)),
                ("Members", str(len(role.members))),
                ("Permissions", ", ".join(permissions[:40]) or "None"),
            ],
        )
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RoleInfoCommand())
