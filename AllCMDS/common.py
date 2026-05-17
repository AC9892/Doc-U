from __future__ import annotations

from datetime import datetime
from random import randint
from typing import Iterable, Sequence

import discord
from discord.ext import commands


DOCS_URL = "https://discordpy.readthedocs.io/en/stable/"
COMMANDS_URL = "https://discordpy.readthedocs.io/en/stable/ext/commands/"
API_URL = "https://discordpy.readthedocs.io/en/stable/api.html"


GUIDE_DETAILS = {
    "channels": {
        "workflow": "Decide whether you need a cached channel, fetched channel, or slash-command channel option. Use cached objects for normal command work, fetch only when the object may not be cached, and always check permissions before sending or editing.",
        "watch": "Do not assume every channel supports `send`. Voice, stage, category, forum, thread, DM, and text channels have different methods and permission behavior.",
        "details": "Channel code usually fails for one of three reasons: the channel type is not what the command expected, the bot lacks channel permissions, or the object is not cached. Prefer explicit annotations like `discord.TextChannel` for slash command options, and use `channel.permissions_for(ctx.guild.me)` before actions that require send, manage, or history permissions.",
    },
    "checks": {
        "workflow": "Put checks closest to the command they protect. Use built-in checks for common Discord permission rules and custom checks for project-specific state such as premium status, guild configuration, or feature flags.",
        "watch": "A user permission check is not enough for moderation commands. The bot also needs matching permissions and must pass role hierarchy checks.",
        "details": "Checks run before the command callback. For prefix commands they raise `commands.CheckFailure` subclasses; for slash commands the app-command check system raises app-command errors. Keep user-facing errors clear so failed checks do not look like internal failures.",
    },
    "cogs": {
        "workflow": "Group one feature area per cog, keep shared feature state on `self`, and load the cog through an extension `setup` function.",
        "watch": "Avoid putting unrelated commands in one huge cog. Large cogs become hard to reload, test, and reason about.",
        "details": "Cogs are the main organization tool for discord.py bots. They can hold commands, listeners, background tasks, local error handlers, and checks. Use `cog_load` for startup work and `cog_unload` for cleanup such as cancelling loops.",
    },
    "components": {
        "workflow": "Create a `discord.ui.View`, add buttons or selects, send it with a message, and handle each component interaction in its callback.",
        "watch": "Component callbacks must respond to the interaction. If work will take time, defer first and send a followup later.",
        "details": "Views own timeout behavior and component callbacks. Persistent views require stable `custom_id` values and must be registered again when the bot starts. Use ephemeral responses for controls that should only affect the clicking user.",
    },
    "converters": {
        "workflow": "Annotate command parameters with the type you want, then let discord.py convert the raw text into that object before your callback runs.",
        "watch": "Prefix converters and slash command option types are not identical. Hybrid commands must use annotations that can map cleanly to slash options.",
        "details": "Converters are powerful for prefix commands because they can parse mentions, IDs, names, booleans, channels, members, roles, and custom formats. If conversion fails, the callback never runs and a command error is raised.",
    },
    "embeds": {
        "workflow": "Build the embed, add fields in readable sections, set footer or timestamp when helpful, then send it with `embed=embed`.",
        "watch": "Discord has embed limits. Long command output should be split into pages instead of one giant embed.",
        "details": "Embeds are best for structured information, not walls of text. Keep field names short, put details in values, and use pagination for command lists, logs, search results, or documentation pages.",
    },
    "errors": {
        "workflow": "Handle expected user errors locally or globally, log unexpected exceptions, and give users a short actionable message.",
        "watch": "Do not expose raw tracebacks publicly in Discord channels. Send them to logs or the owner instead.",
        "details": "Command errors usually fall into parsing, checks, cooldowns, permission failures, and callback exceptions. Keep expected errors friendly and let unexpected errors include enough logging context to debug later.",
    },
    "events": {
        "workflow": "Use `@bot.event` for global lifecycle events and `@commands.Cog.listener()` for feature-specific listeners.",
        "watch": "If you override `on_message`, prefix commands stop working unless you call `await bot.process_commands(message)`.",
        "details": "Events come from Discord gateway payloads. Some events need intents, some need cache, and raw events exist for cases where cached objects are not available. Always consider whether your event depends on privileged intents.",
    },
    "extensions": {
        "workflow": "Put a feature in a module, expose `async def setup(bot)`, and load it with `bot.load_extension`.",
        "watch": "If an extension partially loads and then errors, duplicate commands can remain unless the loader unloads failed extensions.",
        "details": "Extensions are importable Python modules. They are ideal for separating commands into files, reloading features during development, and keeping `Main.py` focused on startup and shared bot configuration.",
    },
    "files": {
        "workflow": "Use `discord.File` for uploads and `discord.Attachment` for files users send to Discord.",
        "watch": "Always validate attachment size, type, and filename before saving user-provided files.",
        "details": "Attachments provide metadata and async helpers for reading or saving. Upload limits vary by Discord server and account capabilities, so commands should handle HTTP errors gracefully.",
    },
    "guilds": {
        "workflow": "Use `ctx.guild` in guild commands, `bot.get_guild(id)` for cached lookup, and fetch APIs when cache is not enough.",
        "watch": "Guild member, role, and channel data can be incomplete without the right intents or cache state.",
        "details": "A guild object is the entry point for server channels, roles, emojis, stickers, members, bans, audit logs, invites, scheduled events, and many moderation actions.",
    },
    "hybridcommands": {
        "workflow": "Write one command callback with `@commands.hybrid_command`, then make sure every parameter can work as a slash option.",
        "watch": "Prefix-only parsing tricks often break slash registration. Keep names lowercase and option types simple.",
        "details": "Hybrid commands are useful when migrating from prefix commands to slash commands. They receive a `commands.Context`, but when invoked as slash commands the context wraps an interaction.",
    },
    "intents": {
        "workflow": "Start with default intents, enable only the events your bot actually needs, then mirror privileged intent settings in the Developer Portal.",
        "watch": "`message_content`, `members`, and `presences` are privileged in many cases and may require verification for large bots.",
        "details": "Intents affect what events Discord sends and what data discord.py can cache. Missing intents often look like broken events, empty member lists, or commands that cannot read message content.",
    },
    "interactions": {
        "workflow": "Respond once with `interaction.response`, then use followups for later messages or after deferring.",
        "watch": "Interactions have response timing limits. Defer if you need to do slower work.",
        "details": "Interactions power slash commands, components, modals, and context menus. Ephemeral messages are only available through interactions, which is why prefix commands cannot be truly ephemeral.",
    },
    "members": {
        "workflow": "Use member parameters when a command needs guild-specific data such as roles, nicknames, join dates, or permissions.",
        "watch": "A `User` is not the same as a `Member`. Users do not have guild roles or guild permissions.",
        "details": "Member availability depends on cache and intents. For one specific member, converters or fetch APIs are usually better than relying on a fully populated member cache.",
    },
    "messages": {
        "workflow": "Use command callbacks for normal bot commands and message listeners only when you need passive message monitoring.",
        "watch": "Message content access requires the message content intent for most bots.",
        "details": "Messages can be sent, replied to, edited, deleted, pinned, reacted to, and inspected for attachments or embeds. For moderation, prefer clear permission checks and audit-log reasons where supported.",
    },
    "moderation": {
        "workflow": "Check user permissions, check bot permissions, check role hierarchy, perform the action, and log the reason.",
        "watch": "Administrator permission does not bypass role hierarchy for actions against members or roles.",
        "details": "Moderation commands should be conservative. Validate the target, prevent self-targeting or owner-targeting mistakes, pass `reason=`, and catch permission errors so users know what failed.",
    },
    "polls": {
        "workflow": "Create a `discord.Poll`, add between 2 and 10 answers, then send it with the `poll=` keyword argument.",
        "watch": "Do not send the poll object as message content. `await ctx.send(poll=poll)` creates a native Discord poll; `await ctx.send(poll)` just sends a string representation.",
        "details": "Native Discord polls require discord.py support for `discord.Poll` and the bot's `send_polls` permission. Poll answer text has Discord limits, and vote tracking events require poll-related intents. Use raw poll vote events when cache state might be incomplete.",
    },
    "reactions": {
        "workflow": "Use message reaction methods for direct actions and raw reaction events for reliable event handling without message cache.",
        "watch": "Cached reaction events will not fire for uncached messages. Use raw events for reaction-role systems.",
        "details": "Reactions are useful for lightweight voting and legacy interaction flows. For new interactive UI, Discord components are usually more reliable and easier to control.",
    },
    "roles": {
        "workflow": "Resolve the member and role, verify hierarchy and permissions, then add or remove the role with a reason.",
        "watch": "The bot cannot manage a role that is higher than or equal to its highest role.",
        "details": "Role permissions combine across all member roles, then channel overwrites modify the final result. Managed roles are controlled by integrations or bots and usually cannot be manually assigned.",
    },
    "slashcommands": {
        "workflow": "Define the command, sync the tree, wait for Discord to show it, then handle invocations through interactions.",
        "watch": "Global sync can take time to appear. Use guild sync while actively developing.",
        "details": "Slash commands have stricter names and option types than prefix commands. They are discoverable in Discord, can be permission-scoped, and support ephemeral responses.",
    },
    "syncguide": {
        "workflow": "Load extensions first, then sync the command tree after all slash and hybrid commands are registered.",
        "watch": "Repeated global syncing during development can cause confusion because old commands may linger while propagation catches up.",
        "details": "Use global sync for production and guild sync for quick development. If commands are renamed, stale commands may need clearing or a fresh sync strategy.",
    },
    "tasks": {
        "workflow": "Create a loop with `@tasks.loop`, start it in `cog_load`, wait for readiness in `before_loop`, and cancel it in `cog_unload`.",
        "watch": "Background loops should handle errors and avoid running before the bot cache is ready.",
        "details": "Tasks are good for reminders, cleanup, polling, scheduled updates, and cache refreshes. Keep long blocking work out of the event loop or move it to an executor.",
    },
    "voice": {
        "workflow": "Verify the user is in voice, connect to that channel, create an audio source, play it, and disconnect when finished.",
        "watch": "Audio playback generally requires FFmpeg and voice dependencies installed on the host.",
        "details": "Voice is more environment-sensitive than normal message commands. Handle missing voice state, connection failures, already-connected clients, and cleanup after playback stops.",
    },
    "webhooks": {
        "workflow": "Create or fetch a webhook, send through it with controlled content, and store the URL securely if you need reuse.",
        "watch": "Webhook URLs are secrets. Anyone with the URL can send messages through that webhook.",
        "details": "Webhooks are useful for integrations, logs, deployment notifications, and cross-service messages. For bot-controlled actions, normal bot messages are often simpler and easier to permission.",
    },
}


def random_embed_color() -> discord.Color:
    return discord.Color(randint(0, 0xFFFFFF))


def docs_embed(title: str, description: str, fields: Iterable[Sequence[object]] = ()) -> discord.Embed:
    embed = discord.Embed(
        title=title,
        description=description,
        color=random_embed_color(),
        timestamp=discord.utils.utcnow(),
    )
    for field in fields:
        if len(field) < 2:
            continue
        name = str(field[0])
        value = str(field[1])
        inline = bool(field[2]) if len(field) >= 3 else False
        embed.add_field(name=name, value=value[:1024], inline=inline)
    embed.set_footer(text="discord.py reference bot")
    return embed


class GuideExampleView(discord.ui.View):
    def __init__(self, author_id: int, example: str, details: str) -> None:
        super().__init__(timeout=180)
        self.author_id = author_id
        self.example = example
        self.details = details

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id == self.author_id:
            return True
        await interaction.response.send_message("Only the guide requester can use this button.", ephemeral=True)
        return False

    @discord.ui.button(label="Show Example", style=discord.ButtonStyle.primary)
    async def show_example(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        embed = docs_embed("Guide Example", self.example)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="More Details", style=discord.ButtonStyle.secondary)
    async def show_details(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        embed = docs_embed("Guide Details", self.details)
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def send_guide(ctx: commands.Context, embed: discord.Embed, example: str) -> None:
    command_name = ctx.command.name if ctx.command else ""
    detail_data = GUIDE_DETAILS.get(command_name, {})
    workflow = detail_data.get("workflow")
    watch = detail_data.get("watch")
    details = detail_data.get("details", "No extra details are registered for this guide yet.")
    if workflow:
        embed.add_field(name="Practical workflow", value=workflow[:1024], inline=False)
    if watch:
        embed.add_field(name="Common mistakes", value=watch[:1024], inline=False)
    view = GuideExampleView(ctx.author.id, example, details)
    should_be_ephemeral = bool(getattr(ctx.bot, "guide_commands_ephemeral", True))
    if ctx.interaction:
        await ctx.interaction.response.send_message(embed=embed, view=view, ephemeral=should_be_ephemeral)
        return
    await ctx.reply(embed=embed, view=view, mention_author=False)


def human_timedelta(start: datetime, end: datetime | None = None) -> str:
    end = end or discord.utils.utcnow()
    seconds = int((end - start).total_seconds())
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    parts.append(f"{seconds}s")
    return " ".join(parts)


DOC_TOPICS = {
    "bot": (
        "Bot",
        "The main client subclass from `discord.ext.commands`. It owns commands, cogs, events, extensions, the command tree, latency, guild cache, and login lifecycle.",
        "https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot",
    ),
    "cog": (
        "Cogs",
        "Cogs group commands, listeners, checks, and shared state into a class. They are the normal way to keep larger bots organized.",
        "https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html",
    ),
    "extension": (
        "Extensions",
        "Extensions are importable Python modules with `async def setup(bot)`. They let the bot load, unload, and reload command files.",
        "https://discordpy.readthedocs.io/en/stable/ext/commands/extensions.html",
    ),
    "slash": (
        "Application Commands",
        "Slash commands are registered on Discord through `bot.tree`. They use interactions and can send ephemeral responses.",
        "https://discordpy.readthedocs.io/en/stable/interactions/api.html",
    ),
    "hybrid": (
        "Hybrid Commands",
        "`commands.hybrid_command` creates one callback that can be invoked as a prefix command and as a slash command.",
        "https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#hybrid-commands",
    ),
    "embed": (
        "Embeds",
        "Embeds are rich message payloads with titles, descriptions, fields, images, thumbnails, colors, authors, and footers.",
        "https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed",
    ),
    "intent": (
        "Intents",
        "Intents control which gateway events and cache data Discord sends to your bot. Some are privileged and must be enabled in the Developer Portal.",
        "https://discordpy.readthedocs.io/en/stable/intents.html",
    ),
    "task": (
        "Tasks",
        "`discord.ext.tasks` provides managed background loops with reconnect handling and before/after hooks.",
        "https://discordpy.readthedocs.io/en/stable/ext/tasks/",
    ),
    "converter": (
        "Converters",
        "Converters transform command text into Python objects such as members, channels, roles, booleans, enums, and custom types.",
        "https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#converters",
    ),
    "check": (
        "Checks",
        "Checks are reusable permission or state gates for commands, such as owner-only, guild-only, role checks, or custom predicates.",
        "https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#checks",
    ),
    "event": (
        "Events",
        "Events are gateway callbacks registered globally with `@bot.event` or inside cogs with `@commands.Cog.listener()`.",
        "https://discordpy.readthedocs.io/en/stable/api.html#event-reference",
    ),
    "interaction": (
        "Interactions",
        "Interactions power slash commands, context menus, buttons, selects, and modals.",
        "https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction",
    ),
    "ui": (
        "discord.ui",
        "The UI kit provides views, buttons, selects, and modals for interactive bot messages.",
        "https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord-ui-kit",
    ),
    "webhook": (
        "Webhooks",
        "Webhooks send messages into channels with configurable names, avatars, embeds, and files.",
        "https://discordpy.readthedocs.io/en/stable/api.html#discord.Webhook",
    ),
}


GLOSSARY = {
    "guild": "A Discord server.",
    "channel": "A text, voice, stage, forum, category, or thread destination inside Discord.",
    "member": "A user as represented inside one guild, including roles, nickname, and guild permissions.",
    "user": "A Discord account independent of any guild.",
    "interaction": "The payload Discord sends when a slash command, component, modal, or context menu is used.",
    "cog": "A class that groups related bot commands, listeners, and state.",
    "extension": "A Python module loaded by the bot, usually containing one cog and a setup function.",
    "intent": "A gateway subscription that controls which events and cache data the bot receives.",
    "converter": "A command parser component that turns text into typed Python values.",
    "embed": "A rich Discord message layout object.",
}
