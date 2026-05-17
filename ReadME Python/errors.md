# errors

Explains command error handling.

Usage: `/errors` or `-errors`

This project uses `Errors.py` to register:
- `on_command_error` for prefix and hybrid prefix calls
- `bot.tree.error` for slash command errors
- owner DM notification for unexpected exceptions

Common handled errors include missing permissions, missing arguments, bad arguments, and bot missing permissions.
