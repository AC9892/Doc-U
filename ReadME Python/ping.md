# ping

Shows the bot websocket latency in milliseconds.

Usage: `/ping` or `-ping`

Notes:
- Uses `bot.latency`.
- This measures Discord gateway heartbeat latency, not full command response time.
- Useful as a quick health check after startup or reconnects.
