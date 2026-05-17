from discord.ext import commands

from .common import docs_embed, send_guide


class IntentsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="intents", description="Explain Discord gateway intents.")
    async def intents(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Gateway Intents",
            "Intents decide which gateway events and cached objects your bot receives.",
            [
                ("Common intents", "`guilds`, `messages`, `reactions`, `members`, `moderation`, `message_content`."),
                ("Privileged intents", "`members`, `presences`, and `message_content` must be enabled in the Developer Portal for many bots."),
                ("Best practice", "Enable only the events you need. Overbroad intents increase memory use and may require verification."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/intents.html"),
            ],
        )
        await send_guide(ctx, embed, "Example intents:\n```py\nintents = discord.Intents.default()\nintents.message_content = True\nintents.members = True\nbot = commands.Bot(command_prefix=\"-\", intents=intents)\n```\nEnable matching privileged intents in the Developer Portal.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(IntentsGuideCommand())
