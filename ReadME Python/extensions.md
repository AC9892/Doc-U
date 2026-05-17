# extensions

Explains discord.py extensions.

Usage: `/extensions` or `-extensions`

Key points:
- Extensions are Python modules loaded by `bot.load_extension`.
- Every command file in `AllCMDS` is an extension.
- Each extension exposes `async def setup(bot)`.
- Extensions keep `Main.py` small and make features reloadable.
