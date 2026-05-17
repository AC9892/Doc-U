import discord
from discord.ext import commands

from .common import docs_embed


class ChannelInfoCommand(commands.Cog):
    @commands.guild_only()
    @commands.hybrid_command(name="channelinfo", description="Show information about a channel.")
    async def channelinfo(
        self,
        ctx: commands.Context,
        channel: discord.TextChannel | None = None,
    ) -> None:
        target = channel or ctx.channel
        fields = [
            ("ID", str(target.id)),
            ("Type", target.__class__.__name__),
            ("Created", discord.utils.format_dt(target.created_at, style="F")),
        ]
        category = getattr(target, "category", None)
        topic = getattr(target, "topic", None)
        fields.append(("Category", category.name if category else "None"))
        if topic:
            fields.append(("Topic", topic))
        embed = docs_embed(f"Channel Info: #{target.name}", "`discord.TextChannel` exposes topic, message history, permissions, and send APIs.", fields)
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ChannelInfoCommand())
