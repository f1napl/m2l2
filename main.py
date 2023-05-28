import discord
from discord.ext import commands
maininfo = '''**Основные принципы предотвращения загрязнения природы при выбрасывании мусора.**
1. Для установления типа выбрасываемого предмета, обратите внимание на задную этикетку предмета.
Если на ней изображен знак огня:
    Это огнеопасный предмет.
Если на ней изображен знак переработки:
    Это перерабатываемый предмет.
Если на ней изображен знак переработки в квадрате или перечеркнутой мусорки:
    Это неперерабатываемый предмет.

2. **Неперерабатываемые предметы НЕЛЬЗЯ выбрасывать в мусорку, их нужно сдавать в спец. пункты.**
3. **Огнеопасные предметы НЕЛЬЗЯ выбрасывать в мусорку, их нужно сдавать в спец. пункты.**
4. Предметы неперерабатываегомого и огнеопасного типа нельзя вскрывать, ломать, как-либо воздействовать на них.
5. При выбросе перерабатываемого предмета, нужно сортировать их по разным типам (картон,стекло,метал,пластик (абс и пла), и т.д.).
6. При выбросе электроники, ее нужно сдать в спец. пункт (иначе придет штраф).


|| Снизу есть картинки, для того что-бы можно было удостоверится в типе предмета. ||
'''

help = '''Данный бот поможет вам советом, как правильно выбросить мусор.'''
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents)
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
async def help(ctx):
    await ctx.send(help)
bot.run("1234")
