import logging
import discord


# Add more complex logging in future
class DiscLog:
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    def __init__(self) -> None:
        
        pass