# `/doccategory` Command

`/doccategory` shows every catalog entry inside one documentation category. It is useful when you want to browse a whole area of discord.py without guessing exact API names.

This command is implemented in `AllCMDS/doc_category.py`. Category data is stored in `AllCMDS/doc_catalog.py`.

Official discord.py references:

- [discord.py documentation home](https://discordpy.readthedocs.io/en/stable/)
- [discord.py API reference](https://discordpy.readthedocs.io/en/stable/api.html)
- [discord.ext.commands API](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html)
- [Interactions and application commands API](https://discordpy.readthedocs.io/en/stable/interactions/api.html)
- [discord UI kit](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord-ui-kit)

## What The Command Does

`/doccategory` accepts a category key and returns an embed containing:

- the category title
- the official documentation link for that category
- every topic key in that category
- the API name for each entry
- a summary for each entry
- a direct official documentation hyperlink

It is a browsing command. If `/apiref` is for one item, `/doccategory` is for the whole shelf.

## Usage

Slash command:

```text
/doccategory category:commands
```

Prefix command:

```text
-doccategory commands
```

## Available Categories

`guides` contains documentation pages such as quickstart, logging, intents, commands, cogs, extensions, tasks, FAQ, migrating, and version guarantees. Official root: [discord.py documentation home](https://discordpy.readthedocs.io/en/stable/).

`events` contains event callback references such as `on_ready`, `on_message`, `on_interaction`, `on_member_join`, raw reaction events, poll vote events, and voice state updates. Official root: [event reference](https://discordpy.readthedocs.io/en/stable/api.html#event-reference).

`core` contains core objects such as `discord.Client`, `discord.Intents`, `discord.Permissions`, `discord.AllowedMentions`, and utility helpers. Official root: [API reference](https://discordpy.readthedocs.io/en/stable/api.html).

`models` contains Discord model classes such as `discord.Guild`, `discord.Member`, `discord.Message`, `discord.Role`, `discord.Embed`, `discord.Poll`, invites, stickers, audit log entries, and scheduled events. Official root: [Discord API models](https://discordpy.readthedocs.io/en/stable/api.html#discord-api-models).

`channels` contains channel and webhook classes such as `discord.TextChannel`, `discord.VoiceChannel`, `discord.Thread`, `discord.ForumChannel`, `discord.DMChannel`, and `discord.Webhook`. Official root: [API reference](https://discordpy.readthedocs.io/en/stable/api.html).

`commands` contains the `discord.ext.commands` extension, including `commands.Bot`, `commands.Context`, `commands.Command`, `commands.Cog`, checks, cooldowns, converters, and help command classes. Official root: [commands API](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html).

`app_commands` contains slash command and application command objects such as `discord.Interaction`, `app_commands.CommandTree`, `app_commands.Command`, `app_commands.Group`, transformers, choices, ranges, and app command checks. Official root: [interactions API](https://discordpy.readthedocs.io/en/stable/interactions/api.html).

`ui` contains Discord UI classes such as `discord.ui.View`, `discord.ui.Button`, `discord.ui.Select`, `discord.ui.Modal`, `discord.ui.TextInput`, and persistent/dynamic item tools. Official root: [discord UI kit](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord-ui-kit).

`tasks` contains `discord.ext.tasks` helpers such as `tasks.loop` and `tasks.Loop`. Official root: [tasks extension](https://discordpy.readthedocs.io/en/stable/ext/tasks/).

`voice` contains voice client and audio source references such as `discord.VoiceClient`, `discord.AudioSource`, `discord.FFmpegPCMAudio`, and `discord.PCMVolumeTransformer`. Official root: [voice API](https://discordpy.readthedocs.io/en/stable/api.html#voice).

`exceptions` contains base and common exceptions such as `discord.DiscordException`, `discord.HTTPException`, `discord.Forbidden`, `commands.CommandError`, `commands.BadArgument`, and app command errors. Official root: [exceptions](https://discordpy.readthedocs.io/en/stable/api.html#exceptions).

## Example Workflows

To explore command-system objects:

```text
/doccategory category:commands
```

Then inspect one result:

```text
/apiref topic:Context
```

To explore slash commands:

```text
/doccategory category:app_commands
```

Then search for a related term:

```text
/docsearch query:choice
```

To explore event names:

```text
/doccategory category:events
```

Then open one event:

```text
/apiref topic:on_message
```

## Response Visibility

When used as a slash command, `/doccategory` responds ephemerally.

When used as a prefix command, `-doccategory` sends a normal channel message.

## Error Behavior

If the category does not exist, the command returns an embed listing the valid category names.

Example invalid category:

```text
/doccategory category:notreal
```

Recommended recovery:

```text
/docindex
```
