from discord.ext import commands

from .common import docs_embed, send_guide


class TasksGuideCommand(commands.Cog):
    @commands.hybrid_command(name="tasks", description="Explain discord.ext.tasks loops.")
    async def tasks(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Background Tasks",
            "`discord.ext.tasks` runs managed background loops for scheduled work.",
            [
                ("Decorator", "`@tasks.loop(seconds=60)` or `@tasks.loop(time=...)`."),
                ("Lifecycle", "Start loops in `cog_load` and cancel them in `cog_unload`."),
                ("Hooks", "`before_loop`, `after_loop`, `error`, `change_interval`, `is_running`."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/ext/tasks/"),
            ],
        )
        await send_guide(ctx, embed, "Example task loop:\n```py\nfrom discord.ext import tasks\n\n@tasks.loop(minutes=5)\nasync def status_loop():\n    print(\"Still running\")\n\n@status_loop.before_loop\nasync def before_status_loop():\n    await bot.wait_until_ready()\n```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TasksGuideCommand())
