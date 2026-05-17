# syncguide

Explains slash command syncing.

Usage: `/syncguide` or `-syncguide`

Key points:
- Slash commands must be synced before users see them.
- `Main.py` calls `bot.tree.sync()` in `on_ready`.
- Guild sync is faster during development.
- Global sync is better for production but can take longer to appear.
