# `/docsearch` Command

`/docsearch` searches the bot's local discord.py documentation catalog. It is the best command to use when you remember part of a name but do not know the exact category or topic key.

This command is implemented in `AllCMDS/doc_search.py`. Search data is stored in `AllCMDS/doc_catalog.py`.

Official discord.py references:

- [discord.py documentation home](https://discordpy.readthedocs.io/en/stable/)
- [discord.py API reference](https://discordpy.readthedocs.io/en/stable/api.html)
- [discord.ext.commands API](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html)
- [Interactions and application commands API](https://discordpy.readthedocs.io/en/stable/interactions/api.html)

## What The Command Does

`/docsearch` accepts a text query and returns up to ten matching catalog entries.

The search checks:

- topic keys, such as `member`, `commandtree`, or `on_message`
- official API names, such as `discord.Member` or `app_commands.CommandTree`
- short summary text, such as `permission`, `interaction`, `poll`, or `webhook`

Each result includes:

- the official API or documentation name
- the local topic key
- a short summary
- a direct official documentation hyperlink

## Usage

Slash command:

```text
/docsearch query:interaction
```

Prefix command:

```text
-docsearch interaction
```

More examples:

```text
/docsearch query:permission
/docsearch query:poll
/docsearch query:webhook
/docsearch query:cooldown
/docsearch query:modal
/docsearch query:member
/docsearch query:exception
```

## Search Examples

Search for `interaction` to find entries related to:

- [discord.Interaction](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction)
- [discord.InteractionResponse](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.InteractionResponse)
- application commands
- UI callbacks

Search for `permission` to find entries related to:

- [discord.Permissions](https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions)
- [discord.PermissionOverwrite](https://discordpy.readthedocs.io/en/stable/api.html#discord.PermissionOverwrite)
- [commands.has_permissions](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.has_permissions)
- [commands.bot_has_permissions](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.bot_has_permissions)

Search for `poll` to find entries related to:

- [discord.Poll](https://discordpy.readthedocs.io/en/stable/api.html#discord.Poll)
- [discord.PollAnswer](https://discordpy.readthedocs.io/en/stable/api.html#discord.PollAnswer)
- poll vote events
- raw poll vote events

Search for `view` to find entries related to:

- [discord.ui.View](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.View)
- [discord.ui.LayoutView](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.LayoutView)
- Discord UI components

## Response Visibility

When used as a slash command, `/docsearch` responds ephemerally.

When used as a prefix command, `-docsearch` sends a normal channel message.

## No Results Behavior

If no result is found, the bot returns a no-results embed and suggests `/docindex`.

Example:

```text
/docsearch query:notreal
```

Useful next steps:

```text
/docindex
/doccategory category:commands
/docs topic:bot
```

## When To Use Another Command

Use `/docs` when you want a short beginner-friendly explanation of a broad topic.

Use `/apiref` when you already know the exact API name or topic key.

Use `/doccategory` when you want every entry from one category.

Use `/docsources` when you want the official documentation source links.
