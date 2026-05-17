from discord.ext import commands

from .common import docs_embed


class GuideEphemeralToggleCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.is_owner()
    @commands.hybrid_command(
        name="guideephemeral",
        description="Owner only: turn guide command ephemeral replies on or off.",
    )
    async def guideephemeral(self, ctx: commands.Context, enabled: bool) -> None:
        self.bot.guide_commands_ephemeral = enabled
        state = "enabled" if enabled else "disabled"
        embed = docs_embed(
            "Guide Ephemeral Setting",
            f"Guide command ephemeral slash replies are now `{state}`.",
            [
                ("Scope", "Only guide commands use this runtime setting."),
                ("Locked commands", "Commands with their own forced ephemeral behavior, such as `/cmdlist`, are not affected."),
                ("Prefix note", "Prefix commands cannot be ephemeral in Discord."),
            ],
        )
        if ctx.interaction:
            await ctx.interaction.response.send_message(embed=embed, ephemeral=True)
            return
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GuideEphemeralToggleCommand(bot))
