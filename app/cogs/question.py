import discord
from discord import app_commands
from discord.ext import commands
import asyncio
from time import sleep


class ClassName(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="question")
    async def question(self, ctx: commands.Context, message: str) -> None:
        def is_requester(msg):
            return msg.author == ctx.author

        total_deleted = 0
        limit_per_round = 1  # 各ループで削除するメッセージの最大数
        target_deletion_count = 100  # 削除したいメッセージの総数

        while total_deleted < target_deletion_count:
            deleted = await ctx.channel.purge(limit=limit_per_round, check=is_requester)
            total_deleted += len(deleted)

            if len(deleted) < limit_per_round:
                break

            sleep(2)

        deleted = await ctx.channel.purge(limit=100, check=is_requester)
        await ctx.send(f"command is not working ...", delete_after=1, ephemeral=True)

    # @app_commands.command(name="question")
    # async def slash_question(self, interaction: discord.Interaction, message: str) -> None:
    #     channel = interaction.guild.get_channel_or_thread(interaction.channel_id)
    #     await channel.send(message)
    #     await interaction.response.send_message("質問を送信しました", ephemeral=True)
    #     return


async def setup(bot: commands.Bot):
    await bot.add_cog(ClassName(bot=bot))
    await bot.tree.sync()
