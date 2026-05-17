from discord.ext import commands

from .common import docs_embed, send_guide


class FilesGuideCommand(commands.Cog):
    @commands.hybrid_command(name="files", description="Explain sending files and attachments.")
    async def files(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Files and Attachments",
            "discord.py can upload local files with `discord.File` and inspect received files as `discord.Attachment`.",
            [
                ("Sending", "Use `await channel.send(file=discord.File(path))` or pass multiple files with `files=[...]`."),
                ("Receiving", "Message attachments expose filename, URL, size, content type, and async save/read helpers."),
                ("Limits", "Upload size depends on the guild and account limits Discord applies."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#discord.File"),
            ],
        )
        await send_guide(ctx, embed, "Example file upload:\n```py\nawait ctx.reply(file=discord.File(\"report.txt\"))\n```\nExample attachment save:\n```py\nawait message.attachments[0].save(\"upload.png\")\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(FilesGuideCommand())
