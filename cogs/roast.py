import discord
from discord.ext import commands
import requests, json


'''
Gets a random insult from API (https://evilinsult.com/api/)

JSON Structure:
{
  "number": "123",
  "language": "en",
  "insult": "This will be the insult",
  "created": "2018-10-24 06:52:02",
  "shown": "2688",
  "createdby": "someone",
  "active": "1",
  "comment": "Sourced from some website"
}

'''
class Roast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Command Roast is ready")

    @commands.command()
    async def roast(self, ctx):
        try:
            api_response  = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
            #print("response code is " + str(api_response.status_code))
            json_data = json.loads(api_response.text)
            #print(json_data)
            quote     = json_data['insult'] #+ " created by " + json_data['createdby']
            await ctx.send(quote)
        except:
            await ctx.send("Cannot roast")

async def setup(bot):
    await bot.add_cog(Roast(bot))