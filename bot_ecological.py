import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def  quiz(ctx):
    await ctx.send("Benvenuto al quiz!")
    await ctx.send("Domanda 1: Quando si butta la spazzatura l'umido?")
    await ctx.send("a) Lunedì e Giovedì")
    await ctx.send("b) Martedì e Venerdì")
    await ctx.send("c) Mercoledì e Sabato")
bot.run("MTU1ODQ5MjMyNjQ2NzM0MjQ0Nw.GjGSCM.v7Y62ASi6SwcWCOAmhC_8aFvYXq47oGbI5SW5o")