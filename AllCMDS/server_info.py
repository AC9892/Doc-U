import discord
from discord.ext import commands

from .common import docs_embed


class ServerInfoCommand(commands.Cog):
    @commands.guild_only()
    @commands.hybrid_command(name="serverinfo", description="Show information about this server.")
    async def serverinfo(self, ctx: commands.Context) -> None:
        guild = ctx.guild
        embed = docs_embed(
            f"Server Info: {guild.name}",
            "`discord.Guild` represents a Discord server.",
            [
                ("ID", str(guild.id)),
                ("Owner", guild.owner.mention if guild.owner else "Unknown"),
                ("Created", discord.utils.format_dt(guild.created_at, style="F")),
                ("Members", str(guild.member_count)),
                ("Channels", f"{len(guild.text_channels)} text, {len(guild.voice_channels)} voice, {len(guild.categories)} categories"),
                ("Roles", str(len(guild.roles))),
                ("Boost level", str(guild.premium_tier)),
            ],
        )
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ServerInfoCommand())
