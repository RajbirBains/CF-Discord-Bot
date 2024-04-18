import discord
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Command Test is ready")
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Testing")

async def setup(bot):
    await bot.add_cog(Test(bot))