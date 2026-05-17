from discord.ext import commands

from .common import docs_embed, send_guide


class MembersGuideCommand(commands.Cog):
    @commands.hybrid_command(name="members", description="Explain member objects and member intent.")
    async def members(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Members",
            "`discord.Member` is a user inside a guild, including roles, nicknames, guild avatar, and permissions.",
            [
                ("Cache", "Member data may be partial unless the members intent is enabled and the cache has been populated."),
                ("Fetching", "Use `Guild.fetch_member` for one member or `Guild.chunk`/member intent for broader cache needs."),
                ("Permissions", "Use `channel.permissions_for(member)` for final channel permissions."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#discord.Member"),
            ],
        )
        await send_guide(ctx, embed, "Example member command:\n```py\n@commands.hybrid_command(name=\"joined\")\nasync def joined(self, ctx, member: discord.Member):\n    await ctx.reply(discord.utils.format_dt(member.joined_at, style=\"F\"))\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MembersGuideCommand())
