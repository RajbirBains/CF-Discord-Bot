"""
Discord bot 
Rajbir Bains

Future projects
- replace prints with logging system
- move everything from one file to multiple files/classes


Notes:

"""

import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, VoiceChannel, VoiceState
from discord.ext import commands
from other.responses import get_response
from other.botlogging import DiscLog
import asyncio

#import json, requests
#import random, time

COMMAND_PREFIX = '!'


load_dotenv(dotenv_path='venv/.env') # Loading token from env file
TOKEN = os.getenv('DISCORD_TOKEN') # token - sensitive information that links the bot

#print(TOKEN) only printed for debugging, token is sensitive info do not uncomment


# Set up the bot
intent = Intents.default() # intent - defines what capabilities the bot has (read msgs, join voice channel, etc)
intent.message_content = True
bot = commands.Bot(command_prefix = COMMAND_PREFIX, intents= intent)


# Loads cogs (commands) from cogs file
async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[ : -3]}")


@bot.event  # @bot.event is an event listener for the bot - listens for specific event defined by function name (eg. async def on_member_join()) # list of other events found here https://discordpy.readthedocs.io/en/stable/api.html
async def on_ready():
    print(f'{bot.user} is now running') # Bot will print in console when started


def main():
    cLog = DiscLog() # log for errors (Add more complex later)

    asyncio.run(load_cogs())
    bot.run(token = TOKEN, log_handler= cLog.handler) # runs the bot

    return 0

main()








'''
Unused code section? Code that I used before that I am not sure what to do with yet



"""
Message functionality
    is_private - if user's first input is ? followed by a message, the response will be send in DM instead of in channel
    user_msg   - message of any user in the discord
    get_response - function that outputs a response depending on user input (eg. User says hello in sentence, bot will respond with "Hi!")
"""
async def send_message(message : Message, user_msg : str): #async allows co-routines/concurrency (allows multiple tasks to run without having to wait for another to finish)
    if not user_msg:
        print("Message was empty because intent was not enabled")
    
    """
    REMOVING DM FUNCTIONALITY FOR NOW
    if is_private := user_msg[0] == "?": # Walrus Operator (:=) allows you to assign a value to a variable within an expression
        user_msg = user_msg[1:]
    """
    try:
        response : str = get_response(user_msg)
        await message.channel.send(response) # sends response into channel

        #await message.author.send(response) if is_private else await message.channel.send(response) REMOVING DM FUNCTIONALITY FOR NOW
    except Exception as err:
        print(err) 






"""
Handling incoming messages 
    Bot listens for any input in channel
    channel - the channel the bot is currently reading from 
    client - bot
"""

"""
@bot.event
async def on_message(message):
    # ignore messages from bot to avoid infinite loop of responses
    if message.author == bot.user:
        return
    
    channel = message.channel
    username = str(message.author)
    user_msg = message.content 
    
    if user_msg[0] == COMMAND_PREFIX:
        if user_msg[1:0] in commands_list:
            return
    
    print(f'[{channel}] {username} : {user_msg}')
    await send_message(message, user_msg)
"""






'''