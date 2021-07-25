# Import things
import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

# Set bot prefix
prefix = "#"

# Set client variable, which will use to control event and commands
client = commands.Bot(command_prefix = prefix)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'Functions.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'Functions.{extension}')
    client.load_extension(f'Functions.{extension}')


for filename in os.listdir('./Functions'):
    if filename.endswith('.py'):
        client.load_extension('Functions.{}'.format(filename[:-3]))


# Event happened
@client.event
# If the bot is ready
async def on_ready():
    print("Bot is ready! Logged in as {0.user}".format(client))

@client.command()
# Command received
# If it is the ping command
async def ping(ctx):
    # Respond pong and the latency
    await ctx.send(f"```Pong!\nLatency: {round(client.latency * 1000)}ms```")

# Command received
@client.command()
#If it is a help command
async def helps(ctx):
    # Respond the help text to command author
    await ctx.send(f'''
    ```    Hello {ctx.author}. This is AM Testing Bot. The bot where you can find a lot of features.
    *Disclamer: This bot is still in the beta stage, we are still making the bot more useful. So stay tuned*
    Version: 1.0.1

    Supported commands:
    #help: Show this help
    #hello or #hi: Say hello to yourself.
    #inspire: Some random English quote that I don't want to read
    #ping: Pong!
    #kick: Kick a member
    #ban: Ban a member
    #cls: Clear bulk messages```
    ''')

# Keep alive on repl.it server
keep_alive()

# Bot token, getting from the environment variables
TOKEN = os.environ["TOKEN"]
#TOKEN = os.getenv('TOKEN')

# Run the bot
client.run(TOKEN)