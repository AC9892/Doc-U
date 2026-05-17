from discord.ext import commands

from .common import docs_embed, send_guide


class WebhooksGuideCommand(commands.Cog):
    @commands.hybrid_command(name="webhooks", description="Explain Discord webhooks.")
    async def webhooks(self, ctx: commands.Context) -> None:
        embed = docs_embed(
            "Webhooks",
            "Webhooks send messages through a channel without using a normal bot command flow.",
            [
                ("Creating/fetching", "Channels expose webhook management APIs when the bot has `manage_webhooks`."),
                ("Sending", "`Webhook.send` can customize username, avatar, embeds, files, and allowed mentions."),
                ("Security", "Treat webhook URLs like tokens. Anyone with the URL can send through it."),
                ("Reference", "https://discordpy.readthedocs.io/en/stable/api.html#discord.Webhook"),
            ],
        )
        await send_guide(ctx, embed, "Example webhook send:\n```py\nwebhook = await channel.create_webhook(name=\"Updates\")\nawait webhook.send(\"Deployment complete\", username=\"Deploy Bot\")\n```\nKeep webhook URLs private.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WebhooksGuideCommand())
