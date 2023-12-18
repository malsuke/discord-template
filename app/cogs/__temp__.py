import discord
from discord import app_commands
from discord.ext import commands


class ClassName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="command_name")
    async def command_name(self, ctx: commands.Context) -> None:
        """
        !<command_name>の形式で実行されるコマンド
        """
        pass

    @app_commands.command(name="command_name")
    async def slash_command_name(self, interaction: discord.Interaction) -> None:
        """
        /<command_name>の形式で実行されるコマンド
        """
        pass


async def setup(bot: commands.Bot):
    await bot.add_cog(ClassName(bot=bot))
    await bot.tree.sync()
