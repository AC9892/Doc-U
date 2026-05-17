from discord.ext import commands

from .common import docs_embed, send_guide


class GuildsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="guilds", description="Explain guild/server objects.")
    async def guilds(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Guilds",
            "`discord.Guild` represents a Discord server and exposes channels, roles, members, emojis, stickers, and moderation APIs.",
            [
                ("Cache access", "`bot.guilds`, `bot.get_guild(id)`, `guild.channels`, `guild.roles`, `guild.members`."),
                ("Network access", "`bot.fetch_guild(id)` fetches API data when the object is not cached."),
                ("Mutations", "Guild edits and moderation actions require both bot permissions and role hierarchy."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild"),
            ],
        )
        await send_guide(ctx, embed, "Example guild access:\n```py\nguild = ctx.guild\nawait ctx.reply(f\"{guild.name} has {guild.member_count} members\")\n```\nUse `bot.get_guild(id)` for cached lookup.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GuildsGuideCommand())
