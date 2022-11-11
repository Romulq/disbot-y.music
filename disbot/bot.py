import discord
from discord.ext import commands

config = {
    'token': 'token',
    'prefix': '!',
}

bot = commands.Bot(intents=discord.Intents.default(), command_prefix=config['prefix'])

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет Чумба!')

bot.run(config['token'])


