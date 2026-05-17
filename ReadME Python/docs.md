# `/docs` Command

`/docs` is the fast topic lookup command for common discord.py concepts. It is meant for users who want a short explanation and an official documentation link without searching through the full API catalog.

This command is implemented in `AllCMDS/docs.py`. Topic data comes from `AllCMDS/common.py`.

Official discord.py documentation:

- [discord.py documentation home](https://discordpy.readthedocs.io/en/stable/)
- [discord.ext.commands guide](https://discordpy.readthedocs.io/en/stable/ext/commands/)
- [Interactions and application commands](https://discordpy.readthedocs.io/en/stable/interactions/api.html)
- [discord.ext.tasks](https://discordpy.readthedocs.io/en/stable/ext/tasks/)
- [Intents guide](https://discordpy.readthedocs.io/en/stable/intents.html)

## What The Command Does

`/docs` accepts a topic name and returns an embed containing:

- the topic title
- a short plain-English explanation
- a direct official discord.py reference link

It is intentionally smaller than `/docsearch` and `/apiref`. Use `/docs` for broad learning topics. Use `/apiref` when you want a specific class, exception, event, decorator, or object.

## Usage

Slash command:

```text
/docs topic:bot
```

Prefix command:

```text
-docs bot
```

If no topic is provided, the command defaults to:

```text
bot
```

## Supported Topics

`bot` explains the main `commands.Bot` client and links to [commands.Bot](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot).

`cog` explains command organization with cogs and links to the [cogs guide](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html).

`extension` explains loadable command modules and links to the [extensions guide](https://discordpy.readthedocs.io/en/stable/ext/commands/extensions.html).

`slash` explains slash commands and interactions and links to [interactions API documentation](https://discordpy.readthedocs.io/en/stable/interactions/api.html).

`hybrid` explains commands that work as both prefix and slash commands and links to [hybrid command documentation](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#hybrid-commands).

`embed` explains rich Discord embeds and links to [discord.Embed](https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed).

`intent` explains gateway intents and links to the [intents guide](https://discordpy.readthedocs.io/en/stable/intents.html).

`task` explains managed background loops and links to [discord.ext.tasks](https://discordpy.readthedocs.io/en/stable/ext/tasks/).

`converter` explains command argument converters and links to [converter documentation](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#converters).

`check` explains command checks and links to [checks documentation](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#checks).

`event` explains gateway event callbacks and links to the [event reference](https://discordpy.readthedocs.io/en/stable/api.html#event-reference).

`interaction` explains interaction payloads and links to [discord.Interaction](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction).

`ui` explains views, buttons, selects, and modals and links to the [discord UI kit](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord-ui-kit).

`webhook` explains Discord webhooks and links to [discord.Webhook](https://discordpy.readthedocs.io/en/stable/api.html#discord.Webhook).

## Example Use Cases

Use `/docs topic:intent` when a bot event is not firing and you need to check whether a privileged intent may be missing.

Use `/docs topic:hybrid` when you want one callback to work as both `/command` and `-command`.

Use `/docs topic:ui` when you are adding buttons, select menus, views, or modals.

Use `/docs topic:task` when you need a background loop for reminders, cleanup, polling, or scheduled jobs.

## Error Behavior

If the user enters an unknown topic, the command replies with the available topic names.

Unknown topic example:

```text
/docs topic:notreal
```

The bot will not crash. It will return a short message telling the user which topics are valid.

## When To Use Another Command

Use `/docindex` if you do not know what categories are available.

Use `/doccategory` if you want every entry in one category.

Use `/docsearch` if you remember only part of a name.

Use `/apiref` if you already know the exact API class, event, or decorator.
