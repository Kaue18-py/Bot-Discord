import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()                      
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True     

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

@bot.command()
async def ola(ctx):
    await ctx.send(f"Olá, {ctx.author.display_name}!")
@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)

    if numero == 1:
        cor = discord.Color.red()
    elif numero == 6:
        cor = discord.Color.green()
    else:
        cor = discord.Color.blue()

    embed = discord.Embed(
        title="🎲 Rolagem de dado",
        description=f"Você tirou **{numero}**!",
        color=cor
    )

    embed.set_footer(text=f"Pedido por {ctx.author.display_name}")

    await ctx.send(embed=embed)
bot.run(TOKEN)