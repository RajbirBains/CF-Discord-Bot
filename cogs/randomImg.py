import discord
from discord.ext import commands
import json, requests

'''
Todo:
Add functionality to have different animals in same command
Ex. !rimg dog, !rimg cat

Create a new class in seperate files that handles all API calls (Cleaner code)
'''

class RandomImage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Command RandomImg is ready")
    

    '''
    Gets a random insult from API (https://dog.ceo/dog-api/)

    JSON Structure:
    {
    "message": "https://images.dog.ceo/breeds/spaniel-blenheim/n02086646_1825.jpg",
    "status": "success"
    }

    '''
    @commands.command(name="rdog")
    async def rImg(self, ctx):
        try:
            api_response = requests.get("https://dog.ceo/api/breeds/image/random")
            print("response code is " + str(api_response.status_code))
            json_data = json.loads(api_response.text)
            print(json_data)
            quote = json_data["message"]
            await ctx.send(quote)
        except:
            await ctx.send("Cennot produce random image")
            print("Random image failed")


async def setup(bot):
    await bot.add_cog(RandomImage(bot))
