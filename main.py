# Project Name: AM_1909A
# Application Name: AM Testing Bot
# Creation Date: Sun Jul 25 09:45:23 ICT 2021
# Creator: AM

# Import things
import discord
import os
import requests
import json
from keep_alive import keep_alive

# Set discord client to interact with discord API (via discord.py)
client = discord.Client()

# Set prefix for bot
prefix = "#"

# Print if bot is ready
@client.event
async def on_ready():
  print("Bot is ready! Logged in as {0.user}".format(client))

# Inspirational Message from API
def get_quote():
  ran_quote = requests.get("https://zenquotes.io/api/random")
  json_quote = json.loads(ran_quote.text)
  quote = json_quote[0]['q'] + " - " + json_quote[0]['a']
  return quote

# Event if bot receive a message
@client.event
async def on_message(message):
  # If that is the bot's own message
  if message.author == client.user:
    return

  # If that is the command "Hello"
  if message.content.startswith("{}hello".format(prefix)) or message.content.startswith("{}hi".format(prefix)):
    await message.channel.send("Hello!!!")

  # If that is the command "Inspire"
  if message.content.startswith("{}inspire".format(prefix)):
    quote = get_quote()
    await message.channel.send(quote)

  # If that is the command "Help"
  if message.content.startswith("{}help".format(prefix)):
    await message.channel.send('''
    ```Hello {0.author}. This is AM Testing Bot. The bot where you can find a lot of features.
    *Disclamer: This bot is still in the beta stage, we are still making the bot more useful. So stay tuned*
    Version: 1.0.0

    Supported commands:
    #help: Show this help
    #hello or #hi: Say hello to yourself.
    #inspire: Some random English quote that I don't want to read```
    '''.format(message))

# Keep the bot alive on repl.it server
keep_alive()

# Run the bot with known token
client.run(os.environ['TOKEN'])

