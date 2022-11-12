import random

import discord
from discord.ext import commands

import config

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix=config.PREFIX)


queue = []


################# CHAT #################

@bot.command()
async def hello(ctx, arg=None):
    if ctx.author.bot:
        return
    
    if arg != None:
        return await ctx.send(f'Привет {arg}')

    await ctx.send('Привет Чумба!')
    
@bot.command()
async def randnum(ctx):

    random_num = str(random.randrange(0, 100))
    
    await ctx.send(f'Кости брошены, {ctx.author.name}! Тебе выпало: {random_num}')
    
########################################


################# VOICE ################

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    
@bot.command()
async def queues(ctx, arg1, arg2=None):
    if arg1 == 'show':
        if len(queue) == 0:
            await ctx.send('Очередь пуста')
            return
        # await ctx.send(f'Очередь треков: {[f"{a}" for a in queue]}')
        await ctx.send(f'Очередь треков: {queue}')
    elif arg1 == 'add':
        queue.append(arg2)
        
    
########################################


################# RUN BOT ##############
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run(config.TOKEN)
########################################
