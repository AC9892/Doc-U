from discord.ext import commands

from .common import docs_embed, send_guide


class MessagesGuideCommand(commands.Cog):
    @commands.hybrid_command(name="messages", description="Explain message commands and events.")
    async def messages(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Messages",
            "Messages are represented by `discord.Message` and are commonly handled by commands or listeners.",
            [
                ("Sending", "Use `ctx.send`, `ctx.reply`, `channel.send`, or interaction responses."),
                ("Receiving", "Use `on_message` carefully. If you override it, call `await bot.process_commands(message)` for prefix commands."),
                ("Message content", "Reading arbitrary content requires the `message_content` privileged intent."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#discord.Message"),
            ],
        )
        await send_guide(ctx, embed, "Example message listener:\n```py\n@bot.event\nasync def on_message(message):\n    if message.author.bot:\n        return\n    await bot.process_commands(message)\n```\nCalling `process_commands` keeps prefix commands working.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MessagesGuideCommand())
