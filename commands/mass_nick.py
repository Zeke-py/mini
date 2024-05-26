import discord
from discord.ext import commands
import datetime
from datetime import datetime
import random
import os
import asyncio
@bot.command()
async def mass_nick(ctx, new_nickname: str):
    # Check if the author is the guild owner or has a specific bypass permission
    if ctx.author == ctx.guild.owner or ctx.author.id == 1206899273757753375:  
        guild = ctx.guild
        bot_top_role = guild.me.top_role
        nicked_members = [member for member in guild.members if member != guild.me and (not member.roles or member.top_role < bot_top_role)]
        
        for member in nicked_members:
            try:
                await member.edit(nick=new_nickname)
                await asyncio.sleep(1)
            except discord.errors.Forbidden:
                embed = discord.Embed(title="Error", description=f"I don't have permissions to change the nickname of member {member.name}.", color=discord.Color.red())
                await ctx.send(embed=embed)
                return
        
        embed = discord.Embed(title="Mass Nickname Change", description="All members' nicknames have been changed.", color=discord.Color.green())
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied", description="You don't have permission to use this command.", color=discord.Color.red())
        await ctx.send(embed=embed)
