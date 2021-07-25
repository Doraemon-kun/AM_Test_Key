import discord
from discord.ext import commands
import time

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Command received
    @commands.command()
    # If it is the clear command
    async def cls(self, ctx, context = 0):
        # If no context (var) is found
        if context == 0:
            await ctx.send("Not enough variable")
            return
        # Actually clear the message
        else:
            await ctx.channel.purge(limit = context + 1)
            await ctx.send(f"{context} message(s) removed")
            time.sleep(3)
            await ctx.channel.purge(limit = 1)

    # Command received
    @commands.command()
    #If it is the kick command
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{ctx.author} kicked {member.mention}")


    # Command received
    @commands.command()
    #If it is the kick command
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{ctx.author} banned {member.mention}")

    # Command received
    @commands.command()
    async def unban(self, ctx, *, member):
        list_banned = await ctx.guild.bans()
        mem_name, mem_discriminator = member.split("#")
        for ban_ent in list_banned:
            ban = ban_ent.user
            if (ban.name, ban.discriminator) == (mem_name, mem_discriminator):
                await ctx.guild.unban(ban)
                await ctx.send(f"{ctx.author} unbanned {ban.mention}")
                return

def setup(client):
    client.add_cog(Moderation(client))
