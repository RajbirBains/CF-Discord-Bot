import discord 
from discord.ext import commands

class CopyMsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Command Copy is ready")

    @commands.command()
    async def copy(self, ctx, *args): # *args allows for multiple/no arguments
        arguments = " ".join(args)
        await ctx.send(f'i aM yOU: ' + arguments)

async def setup(bot):
    await bot.add_cog(CopyMsg(bot))


        