# tasks

Explains `discord.ext.tasks`.

Usage: `/tasks` or `-tasks`

Key points:
- Use `@tasks.loop(...)` for managed background loops.
- Start loops in `cog_load`.
- Cancel loops in `cog_unload`.
- Use `before_loop` to wait for bot readiness.
- Use `error` handlers to log task failures.
