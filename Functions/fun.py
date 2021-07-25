import discord
from discord.ext import commands
import requests
import json

# Inspirational Message from API
def get_quote():
  ran_quote = requests.get("https://zenquotes.io/api/random")
  json_quote = json.loads(ran_quote.text)
  quote = json_quote[0]['q'] + " - " + json_quote[0]['a']
  return quote

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command
    # If it is the inspire command
    async def inspire(self, ctx):
        # Respond a quote to command author
        quote = get_quote()
        await ctx.send(quote)

def setup(client):
    client.add_cog(Fun(client))