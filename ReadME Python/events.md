# events

Explains gateway events and listeners.

Usage: `/events` or `-events`

Highlights:
- `@bot.event` registers global handlers.
- `@commands.Cog.listener()` registers listeners inside cogs.
- `on_ready`, `on_message`, `on_member_join`, and `on_interaction` are common events.
- Prefix bots must call `bot.process_commands(message)` if overriding `on_message`.
