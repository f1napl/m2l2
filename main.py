import discord
from discord.ext import commands
from text import *
links = '''**Википедия со знаками переработки - https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D1%8B_%D0%BF%D0%B5%D1%80%D0%B5%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8**'''
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)
@bot.command()
async def ecology(ctx):
    with open("images/rit.jpg", 'rb') as f:
        picture = discord.File(f)
    with open("images/nonrit.jpg", 'rb') as f:
        picture2 = discord.File(f)
    with open("images/firewarn.jpg", 'rb') as f:
        picture3 = discord.File(f)
    await ctx.send(maininfo)
    await ctx.send(file=picture)
    await ctx.send(file=picture2)
    await ctx.send(file=picture3)
@bot.command()
async def helpme(ctx):
    await ctx.send(helpme)
@bot.command()
async def useful_links(ctx):
    await ctx.send(links)
bot.run(1234)
