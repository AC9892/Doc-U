# Discord.py Documentation Bot

This project is a modular `discord.py` documentation and utility bot. The bot is designed around separate command files in `AllCMDS`, with each command loaded automatically by `Main.py` as a discord.py extension.

The project focuses on three things:

- Teaching discord.py concepts directly inside Discord.
- Providing quick API lookups for common discord.py classes, events, exceptions, decorators, and extension systems.
- Keeping every command separated into its own file so the bot can grow without turning `Main.py` into a large command file.

Official discord.py references:

- [discord.py documentation home](https://discordpy.readthedocs.io/en/stable/)
- [discord.py API reference](https://discordpy.readthedocs.io/en/stable/api.html)
- [discord.ext.commands guide](https://discordpy.readthedocs.io/en/stable/ext/commands/)
- [discord.ext.commands API](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html)
- [Interactions and application commands](https://discordpy.readthedocs.io/en/stable/interactions/api.html)
- [discord.ext.tasks](https://discordpy.readthedocs.io/en/stable/ext/tasks/)
- [discord.py FAQ](https://discordpy.readthedocs.io/en/stable/faq.html)

## Project Layout

`Main.py` creates the bot, configures intents, registers error handlers, loads every command extension from `AllCMDS`, and syncs slash commands.

`Config.py` stores the bot token when you do not want to use the `DISCORD_TOKEN` environment variable.

`Errors.py` registers shared prefix, hybrid, and slash command error handling.

`AllCMDS` contains the bot command modules. Most files expose one command and an `async def setup(bot)` function.

`ReadMe` contains command documentation. The most important documentation-browser commands have their own detailed pages:

- [docs.md](docs.md)
- [apiref.md](apiref.md)
- [doccategory.md](doccategory.md)
- [docsearch.md](docsearch.md)

## Setup

Install Python 3.10 or newer, then install dependencies:

```powershell
pip install -r requirements.txt
```

Set your bot token in one of these places:

```py
# Config.py
Token = "YOUR_TOKEN_HERE"
```

or:

```powershell
$env:DISCORD_TOKEN = "YOUR_TOKEN_HERE"
```

Run the bot from the project root:

```powershell
python Main.py
```

## Discord Developer Portal Requirements

Enable the bot and application command scopes when inviting the bot.

Recommended OAuth2 scopes:

- `bot`
- `applications.commands`

Recommended intents depend on which commands you use. Prefix commands need the Message Content intent. Member-related commands work best with the Members intent. Poll vote events require poll support in your installed discord.py version and matching Discord-side capabilities.

Useful Discord documentation:

- [Discord Developer Portal](https://discord.com/developers/applications)
- [discord.py intents guide](https://discordpy.readthedocs.io/en/stable/intents.html)

## Command Types

Most commands are hybrid commands. That means they can be used as slash commands and as prefix commands.

Slash example:

```text
/docs topic:bot
```

Prefix example:

```text
-docs bot
```

Ephemeral responses only exist for Discord interactions, so only slash command usage can be ephemeral. Prefix commands always send normal Discord messages.

## Documentation Browser Commands

`/docs` is a small topic lookup command for common discord.py concepts such as cogs, extensions, intents, embeds, tasks, and hybrid commands.

`/apiref` is for exact API reference lookups from the local catalog. Use it when you already know what class, event, decorator, or object you want.

`/doccategory` lists every local catalog entry in one documentation category, such as `commands`, `models`, `events`, `app_commands`, `ui`, or `exceptions`.

`/docsearch` searches the local catalog by topic key, API name, and summary text.

`/docindex` shows a paginated category overview.

`/docsources` shows official source links for the documentation used by this bot.

## Guide Commands

Guide commands explain major discord.py systems and include interactive buttons:

- `Show Example` gives a code example.
- `More Details` gives extra implementation notes.

Guide commands are ephemeral by default when used as slash commands. The owner can toggle that runtime behavior with:

```text
/guideephemeral enabled:true
/guideephemeral enabled:false
```

This toggle only affects guide commands. It does not affect commands that are intentionally locked to their own behavior, such as `/cmdlist`.

## Current Command Files

- `api_ref.py` -> `/apiref`
- `avatar.py` -> `/avatar`
- `bot_info.py` -> `/botinfo`
- `channel_info.py` -> `/channelinfo`
- `channels_guide.py` -> `/channels`
- `checks_guide.py` -> `/checks`
- `cogs_guide.py` -> `/cogs`
- `command_list.py` -> `/cmdlist`
- `components_guide.py` -> `/components`
- `converters_guide.py` -> `/converters`
- `doc_category.py` -> `/doccategory`
- `doc_index.py` -> `/docindex`
- `doc_search.py` -> `/docsearch`
- `doc_sources.py` -> `/docsources`
- `docs.py` -> `/docs`
- `embeds_guide.py` -> `/embeds`
- `errors_guide.py` -> `/errors`
- `events_guide.py` -> `/events`
- `extensions_guide.py` -> `/extensions`
- `files_guide.py` -> `/files`
- `glossary.py` -> `/glossary`
- `guide_ephemeral_toggle.py` -> `/guideephemeral`
- `guilds_guide.py` -> `/guilds`
- `help_menu.py` -> `/help`
- `hybrid_commands_guide.py` -> `/hybridcommands`
- `intents_guide.py` -> `/intents`
- `interactions_guide.py` -> `/interactions`
- `invite.py` -> `/invite`
- `members_guide.py` -> `/members`
- `messages_guide.py` -> `/messages`
- `moderation_guide.py` -> `/moderation`
- `permissions.py` -> `/permissions`
- `ping.py` -> `/ping`
- `poll.py` -> `/poll`
- `polls_guide.py` -> `/polls`
- `reactions_guide.py` -> `/reactions`
- `role_info.py` -> `/roleinfo`
- `roles_guide.py` -> `/roles`
- `server_info.py` -> `/serverinfo`
- `slash_commands_guide.py` -> `/slashcommands`
- `sync_guide.py` -> `/syncguide`
- `tasks_guide.py` -> `/tasks`
- `uptime.py` -> `/uptime`
- `user_info.py` -> `/userinfo`
- `voice_guide.py` -> `/voice`
- `webhooks_guide.py` -> `/webhooks`

## Extending The Bot

To add a new command, create a new `.py` file in `AllCMDS` and expose a setup function:

```py
from discord.ext import commands


class ExampleCommand(commands.Cog):
    @commands.hybrid_command(name="example", description="Example command.")
    async def example(self, ctx: commands.Context) -> None:
        await ctx.reply("Example response", mention_author=False)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExampleCommand())
```

Restart the bot. `Main.py` will load the new extension automatically.
