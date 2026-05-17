# slashcommands

Explains Discord application slash commands.

Usage: `/slashcommands` or `-slashcommands`

Key points:
- Slash commands are registered to Discord through `bot.tree`.
- They are invoked as interactions.
- Initial responses use `interaction.response`.
- Later messages use `interaction.followup`.
- Global command sync can take longer than guild sync.
