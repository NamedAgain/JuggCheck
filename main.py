import discord
import os

client = discord.Client()

@client.event
async def ready_on():
    print('{0.user}.format(client)) has logged in')

@client.event
async def jc(message):
    if message.author==client.user:
        return

    if message.content.startswith('$'):
        await message.channel.send('Check your juggs')

client.run(os.getenv('TOKEN'))            