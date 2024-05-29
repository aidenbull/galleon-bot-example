# This example requires the 'message_content' intent.

import discord
import chatgpt

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        response = await chatgpt.perform_request(message.content[1:])
        await message.channel.send(response)
        
client.run('')