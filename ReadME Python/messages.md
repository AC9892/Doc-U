# messages

Explains message models and message handling.

Usage: `/messages` or `-messages`

Key points:
- `discord.Message` represents sent Discord messages.
- Send messages with `ctx.send`, `ctx.reply`, `channel.send`, or interaction responses.
- If you override `on_message`, call `bot.process_commands(message)` to keep prefix commands working.
- Reading arbitrary content requires the message content intent.
