from discord.ext import commands

from .common import docs_embed, send_guide


class VoiceGuideCommand(commands.Cog):
    @commands.hybrid_command(name="voice", description="Explain voice support basics.")
    async def voice(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Voice",
            "discord.py supports connecting to voice channels through voice clients, with optional audio dependencies.",
            [
                ("Connecting", "Use `VoiceChannel.connect()` to create a voice client."),
                ("Playback", "Voice playback generally uses FFmpeg audio sources and requires FFmpeg installed on the host."),
                ("State", "Voice channel/member state is exposed through voice channel and member voice attributes."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#voice"),
            ],
        )
        await send_guide(ctx, embed, "Example voice connect:\n```py\nchannel = ctx.author.voice.channel\nvoice_client = await channel.connect()\n```\nAudio playback usually also needs FFmpeg installed.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(VoiceGuideCommand())
