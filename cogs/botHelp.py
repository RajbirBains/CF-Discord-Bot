import discord
from discord.ext import commands

class BotHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Command Help is ready")

    @commands.command(name="helpme")
    async def help_me(self,ctx):
        help_msg = '''
        Welcome to canucksfan's bot help page                                                                                     
        Use the exclaimation mark (!) to do a command                                                                             
        The following implemented commands are:                                                                                   
            - !test - this command replies with "testing"                                                                         
            - !copy - this command will mimic your text input                                                                     
            - !rps [choice] - this will play a game of rock paper scissors (must choose between "rock", "paper", and "scissors")  
            - !roast - this will make the bot roast you                                                                           
            - !join - bot will join the voice channel (Must be in a voice channel for it to work)                                 
            - !leave - bot will leave the voice channel (Must be in a voice channel for it to work)                               
        '''
        embed_msg = discord.Embed(title="Help", description=help_msg, colour= discord.Colour.blue())
        print("Made it here")
        embed_msg.set_author(name=f"Requested by {ctx.author.mention}")

        await ctx.send(embed =  embed_msg)

async def setup(bot):
    await bot.add_cog(BotHelp(bot))