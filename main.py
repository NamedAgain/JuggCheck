import discord
import os

# client = discord.Client()

# @client.event
# async def ready_on():
#     print('{0.user}.format(client)) has logged in')

# @client.event
# async def jc(message):
#     if message.author==client.user:
#         return

#     if message.content.startswith('.'):
#         await message.channel.send('Check your juggs')

# client.run('ODk3OTg0Nzc2MDA1MzUzNTUy.YWdnfg.Ks_Fl2tuFTiM4_I0TBw7qaFUNHw')            

from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def hello(ctx):
    await ctx.reply('Check your juggs')
bot.run('ODk3OTg0Nzc2MDA1MzUzNTUy.YWdnfg.Ks_Fl2tuFTiM4_I0TBw7qaFUNHw')            
