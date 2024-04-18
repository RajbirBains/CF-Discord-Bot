import discord
from discord.ext import commands

class VoiceChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Voice Channel commands are ready")

    @commands.command(pass_context = True, name="join")
    async def joinVChannel(self,ctx):
        if ctx.author.voice:
            vchannel = ctx.message.author.voice.channel
            vc = await vchannel.connect()
        else:
            await ctx.send("You are not in a voice channel.")

    @commands.command(pass_context = True, name="leave")
    async def leaveVChannel(self,ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("I have left the voice channel")
        else:
            await ctx.send("You are not in a voice channel.")


async def setup(bot):
    await bot.add_cog(VoiceChannel(bot))
