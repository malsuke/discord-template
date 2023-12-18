import discord
from model.user import User
from discord import app_commands
from discord.ext import commands


class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="register")
    async def register(self, ctx: commands.Context):
        await ctx.send(ctx.author.mention)

    @app_commands.command(name="register")
    async def slash_register(self, interaction: discord.Interaction):
        user = User(user_discord_id=interaction.user.id, user_name=interaction.user.name)
        if user.exists_or_create():
            await interaction.response.send_message(f"{user.mention()}さんの登録が完了しました", ephemeral=False)
        else:
            await interaction.response.send_message(f"{user.mention()}さんはすでに登録されています", ephemeral=False)

    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")


async def setup(bot: commands.Bot):
    await bot.add_cog(Register(bot=bot))
    await bot.tree.sync()
