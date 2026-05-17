# guideephemeral

Owner-only runtime setting for guide command visibility.

Usage:
- `/guideephemeral enabled:true`
- `/guideephemeral enabled:false`
- `-guideephemeral true`
- `-guideephemeral false`

Behavior:
- Applies only to guide commands such as `/cogs`, `/intents`, `/tasks`, `/events`, and similar `*_guide.py` commands.
- Does not affect commands that are locked to their own ephemeral behavior, such as `/cmdlist`.
- Does not make prefix command replies ephemeral because Discord only supports ephemeral responses for interactions.
- The setting is runtime-only and resets to enabled when the bot restarts.
