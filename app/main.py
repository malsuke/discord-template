import discord
import os
from dotenv import load_dotenv as ld
from discord.ext import commands


ld()

TOKEN = os.environ["DISCORD_BOT_TOKEN"]
TARGET_GUILD_ID = os.environ["TARGET_GUILD_ID"]

INITIAL_EXTENSIONS = [
    "cogs.register",
    "cogs.mypoint",
    "cogs.point_manager",
    "cogs.question",
]


class Mee10(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def setup_hook(self):
        for extension in INITIAL_EXTENSIONS:
            await self.load_extension(extension)
        await self.tree.sync(guild=discord.Object(id=TARGET_GUILD_ID))


if __name__ == "__main__":
    Mee10().run(TOKEN)
