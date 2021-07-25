import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_joins(self, member):
        print(f"{member} has joined the server!")

    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left the server")

def setup(client):
    client.add_cog(Events(client))