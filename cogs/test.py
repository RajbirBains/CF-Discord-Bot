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
        embedded_msg = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embedded_msg.add_field(name="Field1", value="testing field 1", inline=False)
        await ctx.send(embed = embedded_msg)

    @commands.command()
    async def ping(self, ctx):
        embedded_msg_ping = discord.Embed(title="Bot Ping", description="Latency of bot (ms)", color= discord.Color.blue())
        embedded_msg_ping.add_field(name=f"{self.bot.user.name} latency (ms): ", value= f"{round(self.bot.latency * 1000)} ms" )
        embedded_msg_ping.set_footer(text=f"Requested by {ctx.author.name}", icon_url= ctx.author.avatar)
        await ctx.send(embed = embedded_msg_ping)

async def setup(bot):
    await bot.add_cog(Test(bot))