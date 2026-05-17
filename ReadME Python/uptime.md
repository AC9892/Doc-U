# uptime

Shows how long the bot has been running.

Usage: `/uptime` or `-uptime`

Implementation detail:
- `Main.py` stores `bot.start_time` when the bot object is created.
- The command formats the difference between now and that timestamp.
