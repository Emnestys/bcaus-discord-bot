from discord.ext import commands
import discord
import logging


class Evetime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # An example ready initializer
        logging.info(f'Initialized: {__class__.__name__}')

    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        # an example message listener with cogs
        logging.info('MESSSAGE!')

    @commands.command()
    async def command(self, ctx, arg1: str):
        # an example command with cogs
        await ctx.send(f'You said {arg1}')


async def setup(bot):
    await bot.add_cog(Evetime(bot))