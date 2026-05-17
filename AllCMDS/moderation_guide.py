from discord.ext import commands

from .common import docs_embed, send_guide


class ModerationGuideCommand(commands.Cog):
    @commands.hybrid_command(name="moderation", description="Explain moderation APIs and permission requirements.")
    async def moderation(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Moderation",
            "Discord.py exposes moderation through guild/member methods guarded by Discord permissions and role hierarchy.",
            [
                ("Actions", "`Member.kick`, `Member.ban`, `Guild.ban`, `Member.timeout`, `Message.delete`, `Channel.purge`."),
                ("Requirements", "The bot needs the matching permission and must outrank the target member or role."),
                ("Audit logs", "Pass clear `reason=` values so server audit logs explain what happened."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#discord.Member"),
            ],
        )
        await send_guide(ctx, embed, "Example moderation command:\n```py\n@commands.has_permissions(kick_members=True)\n@commands.hybrid_command(name=\"kick\")\nasync def kick(self, ctx, member: discord.Member, *, reason: str = \"No reason\"):\n    await member.kick(reason=reason)\n    await ctx.reply(\"Member kicked\")\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ModerationGuideCommand())
