from datetime import timedelta
from inspect import signature

import discord
from discord.ext import commands


async def send_poll_error(ctx: commands.Context, message: str) -> None:
    if ctx.interaction:
        if ctx.interaction.response.is_done():
            await ctx.interaction.followup.send(message, ephemeral=True)
        else:
            await ctx.interaction.response.send_message(message, ephemeral=True)
        return
    await ctx.reply(message, mention_author=False)


class PollCommand(commands.Cog):
    @commands.guild_only()
    @commands.bot_has_permissions(send_messages=True)
    @commands.hybrid_command(name="poll", description="Create a real Discord poll, not a reaction poll.")
    async def poll(
        self,
        ctx: commands.Context,
        question: str,
        duration_hours: int,
        allow_multiple: bool,
        answers: str,
    ) -> None:
        if not hasattr(discord, "Poll"):
            await send_poll_error(ctx, "This discord.py version does not support Discord polls. Install a version with `discord.Poll` support.")
            return

        bot_member = ctx.guild.me if ctx.guild else None
        channel_permissions = ctx.channel.permissions_for(bot_member) if bot_member else None
        if channel_permissions and hasattr(channel_permissions, "send_polls") and not channel_permissions.send_polls:
            await send_poll_error(ctx, "I need the `Send Polls` permission in this channel to create a native Discord poll.")
            return

        if not 1 <= duration_hours <= 168:
            await send_poll_error(ctx, "Poll duration must be between `1` and `168` hours.")
            return

        answer_list = [answer.strip() for answer in answers.split("|") if answer.strip()]
        if not 2 <= len(answer_list) <= 10:
            await send_poll_error(ctx, "Provide between `2` and `10` answers, separated with `|`.")
            return

        too_long = [answer for answer in answer_list if len(answer) > 55]
        if too_long:
            await send_poll_error(ctx, "Each poll answer must be `55` characters or fewer.")
            return

        if len(question) > 300:
            await send_poll_error(ctx, "Poll questions must be `300` characters or fewer.")
            return

        poll_kwargs = {"question": question, "duration": timedelta(hours=duration_hours)}
        poll_params = signature(discord.Poll).parameters
        if "allow_multiselect" in poll_params:
            poll_kwargs["allow_multiselect"] = allow_multiple
        elif "multiple" in poll_params:
            poll_kwargs["multiple"] = allow_multiple
        elif "allow_multiple" in poll_params:
            poll_kwargs["allow_multiple"] = allow_multiple
        elif "multiselect" in poll_params:
            poll_kwargs["multiselect"] = allow_multiple

        try:
            poll = discord.Poll(**poll_kwargs)
        except TypeError:
            poll_kwargs["duration"] = duration_hours
            poll = discord.Poll(**poll_kwargs)
        for answer in answer_list:
            poll.add_answer(text=answer)

        if ctx.interaction:
            await ctx.interaction.response.send_message(poll=poll)
            return
        await ctx.send(poll=poll)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PollCommand())
