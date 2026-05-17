# `/apiref` Command

`/apiref` looks up one exact discord.py API reference entry from the bot's local documentation catalog. It is the best command to use when you already know the class, function, event, decorator, or object you want to inspect.

This command is implemented in `AllCMDS/api_ref.py`. The catalog data is stored in `AllCMDS/doc_catalog.py`.

Official discord.py references:

- [discord.py API reference](https://discordpy.readthedocs.io/en/stable/api.html)
- [discord.ext.commands API](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html)
- [Interactions and application commands API](https://discordpy.readthedocs.io/en/stable/interactions/api.html)
- [discord.ext.tasks API](https://discordpy.readthedocs.io/en/stable/ext/tasks/)

## What The Command Does

`/apiref` searches the local catalog for a matching topic and returns an embed with:

- the official API name
- a short summary
- the catalog category
- the topic key
- a direct official documentation hyperlink

The command checks topic keys, API names, and summaries. It is designed for quick reference, not long tutorials.

## Usage

Slash command:

```text
/apiref topic:discord.Member
```

Prefix command:

```text
-apiref discord.Member
```

Other examples:

```text
/apiref topic:Bot
/apiref topic:CommandTree
/apiref topic:View
/apiref topic:HTTPException
/apiref topic:on_message
/apiref topic:Poll
```

## Useful Lookups

Bot and command system:

- `bot` -> [commands.Bot](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot)
- `context` -> [commands.Context](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Context)
- `command` -> [commands.Command](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Command)
- `hybridcommand` -> [commands.HybridCommand](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.HybridCommand)
- `cog` -> [commands.Cog](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Cog)

Discord models:

- `guild` -> [discord.Guild](https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild)
- `member` -> [discord.Member](https://discordpy.readthedocs.io/en/stable/api.html#discord.Member)
- `message` -> [discord.Message](https://discordpy.readthedocs.io/en/stable/api.html#discord.Message)
- `role` -> [discord.Role](https://discordpy.readthedocs.io/en/stable/api.html#discord.Role)
- `embed` -> [discord.Embed](https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed)
- `poll` -> [discord.Poll](https://discordpy.readthedocs.io/en/stable/api.html#discord.Poll)

Application commands and UI:

- `commandtree` -> [app_commands.CommandTree](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.CommandTree)
- `interaction` -> [discord.Interaction](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction)
- `view` -> [discord.ui.View](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.View)
- `button` -> [discord.ui.Button](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.Button)
- `modal` -> [discord.ui.Modal](https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.Modal)

Events and exceptions:

- `on_ready` -> [on_ready](https://discordpy.readthedocs.io/en/stable/api.html#discord.on_ready)
- `on_message` -> [on_message](https://discordpy.readthedocs.io/en/stable/api.html#discord.on_message)
- `on_interaction` -> [on_interaction](https://discordpy.readthedocs.io/en/stable/api.html#discord.on_interaction)
- `httpexception` -> [discord.HTTPException](https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException)
- `commanderror` -> [commands.CommandError](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.CommandError)

## Response Visibility

When used as a slash command, `/apiref` responds ephemerally. Only the command user can see the result.

When used as a prefix command, `-apiref` sends a normal channel message because Discord does not support ephemeral prefix messages.

## Error Behavior

If no catalog entry is found, the bot returns a friendly not-found embed and suggests using `/docsearch`.

Example:

```text
/apiref topic:unknownthing
```

Recommended next step:

```text
/docsearch query:unknownthing
```

## When To Use Another Command

Use `/docs` for broad conceptual topics.

Use `/docsearch` when you do not know the exact catalog key.

Use `/doccategory` when you want all entries under one category.
