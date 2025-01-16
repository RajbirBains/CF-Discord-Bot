import discord
from discord.ext import commands
import json, requests


class PlayMusic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Command PlayMusic is ready")

    @commands.command()
    async def play(self, ctx, *args): # *args allows for multiple/no arguments
        await ctx.send(f'Filler for play')

async def setup(bot):
    await bot.add_cog(PlayMusic(bot))
