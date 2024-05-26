import discord
from discord.ext import commands
import datetime
from datetime import datetime
import random
import os
import asyncio
@bot.command(aliases=['sav', 'serverav'])
async def serveravatar(ctx, member: discord.Member = None):
    member = member or ctx.author

    if member.guild_avatar:
        embed = discord.Embed(
            title=f"{member.guild.name}'s Server Avatar",
            color=discord.Color.blue()
        )
        embed.set_image(url=member.guild_avatar.url)
        embed.set_author(name=member.guild.name, icon_url=member.guild.icon.url)
        embed.set_footer(text=f"Requested by | {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            description=f"{member.display_name} does not have a server avatar.",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)