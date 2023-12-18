from discord.ext import commands
import discord
from model.point import Point
from model.user import User
import logging

logging.basicConfig(level=logging.INFO)


class PointManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return

        if not message.guild:
            return

        """
        概要:
            メッセージが送信されたチャンネルがprivate_threadであり、かつ送信者が管理者でない場合、returnする
        """
        if message.channel.type == discord.ChannelType.private_thread and message.author.id != 367945919175458817:
            return

        user = User(user_discord_id=message.author.id, user_name=message.author.name)
        user.exists_or_create()

        point = Point(user_id=message.author.id)
        point.add_20_point()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, RawReactionActionEvent: discord.RawReactionActionEvent) -> None:
        if RawReactionActionEvent.member.bot:
            return

        if not RawReactionActionEvent.guild_id:
            return

        user = User(user_discord_id=RawReactionActionEvent.member.id, user_name=RawReactionActionEvent.member.name)
        user.exists_or_create()

        point = Point(user_id=RawReactionActionEvent.member.id)
        point.add_20_point()
        return

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, RawReactionActionEvent: discord.RawReactionActionEvent) -> None:
        if not RawReactionActionEvent.guild_id:
            return

        user = User(user_discord_id=RawReactionActionEvent.user_id, user_name=RawReactionActionEvent.member.name)
        user.exists_or_create()

        point = Point(user_id=RawReactionActionEvent.member.id)
        point.sub_20_point()
        return

    # @app_commands.command(name="give")
    # async def mypoint_command(self, interaction: discord.Interaction, user: discord.User, point: int):
    #     if user.bot:
    #         return
    #     if interaction.user.bot:
    #         return
    #     if point <= 0:
    #         await interaction.response.send_message("マイナスは使えないよ", ephemeral=True)
    #         return

    #     point = Point(user_id=interaction.user.id)
    #     await interaction.response.send_message(f"{point.mention()}さんのポイントは{point.get_point()}です", ephemeral=False)


async def setup(bot: commands.Bot):
    await bot.add_cog(PointManager(bot=bot))
    await bot.tree.sync()
