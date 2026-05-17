from discord.ext import commands

from .common import docs_embed, send_guide


class RolesGuideCommand(commands.Cog):
    @commands.hybrid_command(name="roles", description="Explain role objects and hierarchy.")
    async def roles(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Roles",
            "Roles give members permissions, colors, display hierarchy, and grouping inside a guild.",
            [
                ("Hierarchy", "A bot can only manage roles below its highest role and cannot act on members above/equal to it."),
                ("Permissions", "Role permissions combine at guild level, then channel overwrites adjust final permissions."),
                ("Managed roles", "Integration and bot-managed roles cannot usually be manually assigned."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#discord.Role"),
            ],
        )
        await send_guide(ctx, embed, "Example role add:\n```py\n@commands.has_permissions(manage_roles=True)\nasync def addrole(ctx, member: discord.Member, role: discord.Role):\n    await member.add_roles(role, reason=\"Command used\")\n```\nThe bot role must be higher than the target role.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RolesGuideCommand())
