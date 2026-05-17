from discord.ext import commands

from .common import docs_embed, send_guide


class ChannelsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="channels", description="Explain channel objects.")
    async def channels(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Channels",
            "Discord.py models text, voice, stage, forum, category, DM, and thread channels with specialized classes.",
            [
                ("Sending", "Text-like channels support `send`; voice/stage channels focus on connection and metadata."),
                ("Overwrites", "Guild channels can have permission overwrites for roles and members."),
                ("Threads", "Threads are channel-like objects with parent channels and archive state."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel"),
            ],
        )
        await send_guide(ctx, embed, "Example channel send:\n```py\nchannel = ctx.guild.get_channel(123456789012345678)\nawait channel.send(\"Hello channel\")\n```\nFor slash options, use `discord.TextChannel` when you need a channel parameter.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ChannelsGuideCommand())
