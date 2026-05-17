# permissions

Shows resolved channel permissions for a member.

Usage:
- `/permissions`
- `/permissions member:@Someone`
- `/permissions member:@Someone channel:#general`

Important details:
- Uses `channel.permissions_for(member)`.
- Includes role permissions, channel overwrites, guild ownership, and administrator resolution.
- This command is guild-only.
