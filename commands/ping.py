import discord
from discord.ext import commands
import datetime
import random
import os
import asyncio

@bot.command()
async def ping(ctx):
    """Check bot latency and uptime."""
    member = ctx.author
    latency = bot.latency * 1000  # convert to milliseconds
    uptime = datetime.datetime.utcnow() - bot.start_time
    embed = discord.Embed(title="PING PONG", description=f'Pong! Latency: {latency:.2f}ms | Uptime: {uptime}', timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f"requested by | {member.mention}", icon_url=member.avatar.url)
    await ctx.send(embed=embed)

bot.start_time = datetime.datetime.utcnow()
