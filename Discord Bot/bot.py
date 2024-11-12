import discord
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        # Don't let the bot reply to itself
        if message.author == self.user:
            return

        # Respond to $hello command
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
    
# Set up intents (required for reading messages)
intents = discord.Intents.default()
intents.message_content = True

token = os.getenv('BOT_TOKEN')

if token:
    print('Running...')
    client = MyClient(intents=intents)
    client.run(token)  # Use the token loaded from the .env file
else:
    print('Error: No DISCORD_TOKEN found in the environment variables.')
