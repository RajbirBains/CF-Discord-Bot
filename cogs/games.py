import discord
from discord.ext import commands
import time, random


'''
Class to handle different games

#ToDo: 
- Add handler for multiple arguments?
- Re-name class to better name

'''

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Games commands are ready")

    '''
    Simple rock paper scissors game
    '''
    @commands.command()
    async def rps(self, ctx, arg):
        rps_arr = ["rock", "paper", "scissors"]
        player_choice = arg.lower()

        if player_choice not in rps_arr:
            await ctx.send("Yo, that is not a valid input")
            return

        bot_choice = random.randint(0,2)

        await ctx.send("I pick " + rps_arr[bot_choice])


        time.sleep(0.5) # Adds a delay between outputs

        if player_choice == rps_arr[bot_choice]:
            await ctx.send("I guess it is a tie")
        elif player_choice == "rock" and rps_arr[bot_choice] == "scissors":
            await ctx.send("player wins")
        elif player_choice == "paper" and rps_arr[bot_choice] == "rock":
            await ctx.send("player wins")
        elif player_choice == "scissors" and rps_arr[bot_choice] == "paper":
            await ctx.send("player wins")
        elif player_choice == "rock" and rps_arr[bot_choice] == "paper":
            await ctx.send("I win")
        elif player_choice == "paper" and rps_arr[bot_choice] == "scissors":
            await ctx.send("I win")
        elif player_choice == "scissors" and rps_arr[bot_choice] == "rock":
            await ctx.send("player wins")

        time.sleep(0.5)

        await ctx.send("Good game")

async def setup(bot):
    await bot.add_cog(Game(bot))