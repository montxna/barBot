import discord
import random
from discord.ext import commands




intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix="!", intents=intents)

@client.command(pass_context = True)

async def barbut(ctx, target : discord.Member =None):
    if not target:
        await ctx.send ("Trebuie sa alegi un membru pentru a juca!")
    elif target == ctx.author:
        await ctx.send ("Nu poti juca cu tine insuti!")
    else:

        zar1 = random.randint(1,6)
        zar2 = random.randint(1,6)
        zar3 = random.randint(1,6)
        zar4 = random.randint(1,6)
        if (zar1+zar2 > zar3+zar4):
            embed = discord.Embed(title = "🎲Conti Casino🎲", description= "Ai dat " + str(zar1) +" " + str(zar2) + " iar" + str(target.mention) + " a dat " + str(zar3) + " " + str(zar4) + ".     Ai norocul scris in frunte!", color =  (0xF85252))
        elif (zar1+zar2 == zar3+zar4):
            embed = discord.Embed(title="🎲Conti Casino🎲", description="Ai dat " + str(zar1) + " " + str(
                zar2) + " iar " + str(target.mention) + " a dat " + str(zar3) + " " + str(
                zar4) + " .    Egal!", color=(0xF85252))
        elif (zar1+zar2 < zar3+zar4):
            embed = discord.Embed(title="🎲Conti Casino🎲", description="Ai dat " + str(zar1) + " " + str(
                zar2) + " iar " + str(target.mention) + " a dat " + str(zar3) + " " + str(
                zar4) + ".     Amanet scrie pe tine!", color=(0xF85252))
        await ctx.send(embed = embed)

@client.command()
async def hello(ctx):
    await ctx.send("hello mf")

client.run(token)

