# Something that you don't want to mess around
# Import things
from flask import Flask
from threading import Thread

# Set variables for the web server
app = Flask('')

# If the route is going to the home directory
@app.route('/')
# Show the user that the bot is still alive
def home():
  return "Hello. I am alive!"

# Define run webserver command
def run():
  app.run(host='0.0.0.0', port=8080)

# Make the bot still alive
def keep_alive():
  t = Thread(target=run)
  t.start()