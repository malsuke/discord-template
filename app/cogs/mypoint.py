from discord.ext import commands
from discord import app_commands
import discord
from model.point import Point


class MyPoint(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="mypoint")
    async def mypoint(self, ctx: commands.Context):
        point = Point(user_id=ctx.author.id)
        await ctx.send(f"{point.mention()}さんのポイントは{point.get_point()}です")

    @app_commands.command(name="mypoint")
    async def mypoint_command(self, interaction: discord.Interaction):
        point = Point(user_id=interaction.user.id)
        await interaction.response.send_message(f"{point.mention()}さんのポイントは{point.get_point()}です", ephemeral=False)


async def setup(bot: commands.Bot):
    await bot.add_cog(MyPoint(bot=bot))
    await bot.tree.sync()
