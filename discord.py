import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def как_посадить_кактус (ctx):
    await ctx.send(f'в горшок насыпают дренажный слой и почвосмесь до нижней кромки бортика, делают углубление в центре емкости, устанавливают в лунку кактус, аккуратно расправляя корешки тонким предметом, корневая шейка должна располагаться в уровень с землей, засыпают корешки грунтом {bot.user}!')

@bot.command()
async def как_посадить_клубнику (ctx):
    await ctx.send(f'однорядная, с расстоянием между рядами до одного метра, а между кустами — 25 – 30 сантиметров. Также можно сажать растения ковром — тогда расстояние между кустиками будет 25 – 35 сантиметров. В каждую ямку насыпь столовую ложку пепла и помести туда корень так, чтобы он не загибался {bot.user}!')

@bot.command()
async def как_посадить_капусту (ctx):
    await ctx.send(f'в горшок насыпают дренажный слой и почвосмесь до нижней кромки бортика,делают углубление в центре емкост и устанавливают в лунку кактус, аккуратно расправляя корешки тонким предметом, корневая шейка должна располагаться в уровень с землей, засыпают корешки грунтом {bot.user}!')



@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
    
    
bot.run("MTEyNzUzNzg5MTQ2MDAxMDA2NA.Gt3NPx.hGHvkrkLF9fi251T4tmQ02VO5kDjBK7lpC1AD0")
