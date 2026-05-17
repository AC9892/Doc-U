import discord
from discord.ext import commands


class PingCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name="ping", description="Show bot websocket latency.")
    async def ping(self, ctx: commands.Context) -> None:
        latency_ms = round(self.bot.latency * 1000)
        await ctx.reply(f"Pong. WebSocket latency: `{latency_ms}ms`.", mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PingCommand(bot))
