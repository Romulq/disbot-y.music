import discord
from discord.ext import commands

config = {
    'token': 'MTA0MDU4MTY2NDM0ODMwNzQ5Ng.GmDgEs.Ufq1YN_QcvrWhKyPLH2zOt2TXxs4qkn8FwWuwc',
    'prefix': '!',
}

bot = commands.Bot(intents=discord.Intents.default(), command_prefix=config['prefix'])

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет Чумба!')

bot.run(config['token'])


