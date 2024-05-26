import discord
import random
from discord.ext import commands
import canvacord
import os
import asyncio
from datetime import datetime

@bot.command()
async def rankcard(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        username = user.name + "#" + user.discriminator
        currentxp = 150405
        lastxp = 0
        nextxp = 400000
        current_level = 104
        current_rank = 7
        background = None
        image = await canvacord.rankcard(user=user, username=username, currentxp=currentxp, lastxp=lastxp, nextxp=nextxp, level=current_level, rank=current_rank, background=background, ranklevelsep="|", xpsep="/")
        file = discord.File(filename="rankcard.png", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Rank Card Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def welcomecard(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        image = await canvacord.welcomecard(user=user, background=None, avatarcolor="white", topcolor="white", bottomcolor="white", backgroundcolor="black", font=None, toptext="Welcome {user_name}!", bottomtext="Enjoy your stay in {server}!")
        file = discord.File(filename="welcomecard.png", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Welcome Card Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def triggered(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        image = await canvacord.trigger(user)
        file = discord.File(filename="triggered.gif", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Triggered Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def communism(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        image = await canvacord.communism(user)
        file = discord.File(filename="communism.gif", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Communism Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def jail(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        image = await canvacord.jail(user)
        file = discord.File(filename="jail.png", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Jail Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)
        
@bot.command()
async def gay(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        elif member.id == 1206899273757753375:
            await ctx.send(embed=discord.Embed(title="Gay", description="""You can't spank me, I'm immortal!\n
            I will colonize you\n
            You monotonous mutation\n
            You spontaneous sperm\n
            You sisgendered Sasquatch\n
            You melodramatic maggot\n
            You sociopathic snail\n
            You unimaginative unicorn\n
            You unwitting unworthy\n
            Your head like an excommunicated extract.\n
            You are a fucking fucking fucking fucking fucking fucking fucking\n
            Stop yapping or I will put you to work in contaminated contingency,\n
            and your bloodline will be over.""", color=discord.Color.random()))
            return
        else:
            user = member
        image = await canvacord.gay(user)
        file = discord.File(filename="gay.png", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Gay Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)


@bot.command()
async def hitler(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        image = await canvacord.hitler(user)
        file = discord.File(filename="hitler.png", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Hitler Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def aborted(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        image = await canvacord.aborted(user)
        file = discord.File(filename="aborted.png", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Aborted Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def affect(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        image = await canvacord.affect(user)
        file = discord.File(filename="affect.png", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Affect Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def airpods(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        image = await canvacord.airpods(user)
        file = discord.File(filename="airpods.gif", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Airpods Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def america(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        image = await canvacord.america(user)
        file = discord.File(filename="america.gif", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="America Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def wanted(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        image = await canvacord.wanted(user)
        file = discord.File(filename="wanted.png", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Wanted Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def joke(ctx, member: discord.Member = None):
    try:
        if member is None:
            user = ctx.author
        else:
            user = member
        image = await canvacord.jokeoverhead(user)
        file = discord.File(filename="jokeoverhead.png", fp=image)
        await ctx.send(file=file)
    except Exception as e:
        embed = discord.Embed(title="Joke Error", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)
        
@bot.command()
async def spank(ctx, member: discord.Member = None, member2: discord.Member = None):
    try:
        if member is None and member2 is None:
            await ctx.send(embed=discord.Embed(title="Error", description="You need to mention someone to spank", color=discord.Color.blue()))
        elif member2 is None:  # Only one member mentioned
            if member.id == bot.user.id:
                await ctx.send(embed=discord.Embed(title="Spank", description="""You can't spank me, I'm immortal!
      I will colonize you
      You monotonous mutation
      You spontaneous sperm
      You sisgendered Sasquatch
      You melodramatic maggot
      Your head like an excommunicated extract.
      Stop yapping or I will put you to work in contaminated contingency,
      and your bloodline will be over.""", color=discord.Color.red()))
            else:
                image = await canvacord.spank(ctx.author, member)
                file = discord.File(filename="spank.png", fp=image)
                await ctx.send(file=file)
        else:  # Two members mentioned
            if member.id == bot.user.id or member2.id == bot.user.id:
                await ctx.send(embed=discord.Embed(title="Spank", description="""You can't spank me, I'm immortal!
      I will colonize you
      You monotonous mutation
      You spontaneous sperm
      You sisgendered Sasquatch
      You melodramatic maggot
      Your head like an excommunicated extract.
      Stop yapping or I will put you to work in contaminated contingency,
      and your bloodline will be over.""", color=discord.Color.red()))
            else:
                image = await canvacord.spank(member, member2)
                file = discord.File(filename="spank.png", fp=image)
                await ctx.send(file=file)
    except Exception as e:
        await ctx.send(embed=discord.Embed(title="Spank Error", description=str(e), color=discord.Color.red()))

@client.command()
async def bed(ctx, member: discord.Member = None, member2: discord.Member = None):
    if member is None and member2 is None:
        await ctx.send(embed=discord.Embed(title="Error", description="You need to mention someone to share a bed with", color=discord.Color.blue()))
    elif member2 is None:  # Only one member mentioned
        user1 = ctx.author
        user2 = member
        image = await canvacord.bed(user1, user2)
        file = discord.File(filename="bed.png", fp=image)
        await ctx.send(file=file)
    else:  # Two members mentioned
        user1 = member
        user2 = member2
        image = await canvacord.bed(user1, user2)
        file = discord.File(filename="bed.png", fp=image)
        await ctx.send(file=file)
@client.command()
async def calculate_iq(ctx, member: discord.Member):  # Changed 'discord.member' to 'discord.Member'
    iq = random.randint(50, 100)
    embed = discord.Embed(title="iQ Calculation", description="analysing memory....")
    await ctx.send(embed=embed)
    await asyncio.sleep(2)  # Used 'await' for asyncio.sleep
    embed.description = "analysing brain waves..."
    await ctx.send(embed=embed)
    await asyncio.sleep(1)
    embed.description = "Studying neurons..."
    await ctx.send(embed=embed)
    await asyncio.sleep(1)
    embed.description = "scanning electrical signal"
    await ctx.send(embed=embed)
    await asyncio.sleep(2)
    embed.description = "compiling result.."
    await ctx.send(embed=embed)
    await asyncio.sleep(1)
    if member.id == 1154443670167240815:
        await ctx.send(embed=discord.Embed(title="iQ Calculation", description=f"{member.mention} has an IQ of 2000"))
    else:
        await ctx.send(embed=discord.Embed(title="iQ Calculation", description=f"{member.mention} has an IQ of {iq}"))

        