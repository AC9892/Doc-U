from discord.ext import commands

from .common import docs_embed, send_guide


class PollsGuideCommand(commands.Cog):
    @commands.hybrid_command(name="polls", description="Explain how to create real Discord polls with discord.py.")
    async def polls(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Discord Polls",
            "Discord polls are native poll messages, not reaction-based voting messages.",
            [
                ("Create a poll object", "Use `discord.Poll(question=..., duration=..., allow_multiselect=...)`."),
                ("Add answers", "Use `poll.add_answer(text=\"Option\")`. Discord polls support up to `10` answers."),
                ("Send correctly", "Pass the poll with the keyword argument: `await ctx.send(poll=poll)` or `await interaction.response.send_message(poll=poll)`."),
                ("Permissions", "The bot needs the Discord `send_polls` permission in the target channel."),
                ("Events", "Poll vote events include `on_poll_vote_add`, `on_poll_vote_remove`, `on_raw_poll_vote_add`, and `on_raw_poll_vote_remove`."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#polls"),
            ],
        )
        await send_guide(ctx, embed, "Example native Discord poll command:\n```py\nfrom datetime import timedelta\n\npoll = discord.Poll(\n    question=\"What should we build next?\",\n    duration=timedelta(hours=24),\n    allow_multiselect=False,\n)\npoll.add_answer(text=\"Moderation tools\")\npoll.add_answer(text=\"Music features\")\npoll.add_answer(text=\"Documentation commands\")\nawait ctx.send(poll=poll)\n```\nDo not send the poll object as normal content. Use the `poll=` keyword.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PollsGuideCommand())
