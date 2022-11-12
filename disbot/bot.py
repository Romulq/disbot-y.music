import random

import discord
from discord.ext import commands

import config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix=config.PREFIX)

@bot.command(name='hello')
async def on_message(ctx):
    if ctx.author.bot:
        return

    await ctx.send('Привет Чумба!')
    

@bot.command(name='random')
async def on_message(ctx):

    random_num = str(random.randrange(0, 100))
    
    await ctx.send(f'Кости брошены! Вам выпало: {random_num}')

    
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run(config.TOKEN)


