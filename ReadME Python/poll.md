# poll

Creates a real native Discord poll, not a reaction-based poll.

Usage:
- `/poll question:"Best feature?" duration_hours:24 allow_multiple:false answers:"Docs|Moderation|Polls"`
- `-poll "Best feature?" 24 false Docs|Moderation|Polls`

Arguments:
- `question`: poll question text, up to 300 characters.
- `duration_hours`: poll duration from 1 to 168 hours.
- `allow_multiple`: whether users can select multiple answers.
- `answers`: 2 to 10 answers separated with `|`.

Requirements:
- discord.py version with `discord.Poll`.
- Bot permission: `send_polls`.
- The command sends using the `poll=` keyword so Discord creates a native poll message.
