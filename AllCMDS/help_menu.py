from discord.ext import commands

from .common import docs_embed


class HelpMenuCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name="help", description="List all command categories.")
    async def help(self, ctx: commands.Context) -> None:
        names = sorted(command.qualified_name for command in self.bot.commands if not command.hidden)
        embed = docs_embed(
            "Command Help",
            "Every command is kept in its own file in `AllCMDS`. Use slash commands or the `-` prefix.",
            [
                ("Loaded commands", ", ".join(f"`{name}`" for name in names)),
                ("Full command list", "Use `/cmdlist` for detailed embeds with button pages and a discord.py documentation link."),
                ("Docs commands", "`docs`, `glossary`, `intents`, `cogs`, `extensions`, `slashcommands`, `hybridcommands`, `embeds`, `messages`, `tasks`, `converters`, `checks`, `errors`, `syncguide`, `events`, `interactions`, `components`, `files`, `polls`, `reactions`, `webhooks`, `voice`"),
                ("Reference browser", "`docindex`, `doccategory`, `docsearch`, `apiref`, `docsources`"),
                ("Info commands", "`botinfo`, `uptime`, `userinfo`, `serverinfo`, `channelinfo`, `roleinfo`, `avatar`, `permissions`, `invite`, `ping`, `poll`"),
                ("Owner commands", "`guideephemeral`"),
            ],
        )
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HelpMenuCommand(bot))
