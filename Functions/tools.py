import discord
from discord.ext import commands

class Toolkit(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Command received
    @commands.command(aliases=['hi'])
    # If it is the hello or hi command
    async def hello(self, ctx):
        # Respond hello to the command author
        await ctx.send("Hello!!!")

def setup(client):
    client.add_cog(Toolkit(client))
