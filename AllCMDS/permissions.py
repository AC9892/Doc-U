import discord
from discord.ext import commands

from .common import docs_embed


class PermissionsCommand(commands.Cog):
    @commands.guild_only()
    @commands.hybrid_command(name="permissions", description="Show resolved permissions for a member.")
    async def permissions(
        self,
        ctx: commands.Context,
        member: discord.Member | None = None,
        channel: discord.TextChannel | None = None,
    ) -> None:
        target_member = member or ctx.author
        target_channel = channel or ctx.channel
        perms = target_channel.permissions_for(target_member)
        enabled = [name for name, value in perms if value]
        disabled = [name for name, value in perms if not value]
        embed = docs_embed(
            f"Permissions: {target_member.display_name}",
            "Discord resolves permissions from guild ownership, roles, channel overwrites, and administrator.",
            [
                ("Channel", target_channel.mention),
                ("Enabled", ", ".join(enabled[:45]) or "None"),
                ("Disabled count", str(len(disabled))),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions"),
            ],
        )
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PermissionsCommand())
