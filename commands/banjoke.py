import discord
from discord.ext import commands
import asyncio
from datetime import datetime
@bot.command()
async def banjoke(ctx, *, member: discord.Member):
    author = ctx.author
    response = f"Oops! {ctx.author.mention} tried to ban {member.mention}, but it looks like they slipped on a banana peel and missed! <:jreaper:1187214084224073841>"
    
    embed1 = discord.Embed(
        title="# BAN",
        description=response,
        color=discord.Color.red()
    )
    embed1.set_footer(text=f"requested by | {author.display_name}", icon_url=author.avatar.url)
    
    await ctx.send(embed=embed1)
    
    await asyncio.sleep(5)
    
    embed2 = discord.Embed(
        title="# BAN",
        description=f"{member.mention} has been banned <:jreaper:1187214084224073841>",
        color=discord.Color.red()
    )
    embed2.set_footer(text=f"requested by | {author.display_name}", icon_url=author.avatar.url)
    embed2.timestamp = discord.Embed.Empty
    
    await ctx.send(embed=embed2)
    
    await asyncio.sleep(1)
    
    embed3 = discord.Embed(
        title="# ops",
        description=f"ops he really got banned <a:hmmm:1066966136496869396>",
        color=discord.Color.red()
    )
    embed3.set_footer(text=f"requested by | {author.display_name}", icon_url=author.avatar.url)
    embed3.timestamp = datetime.utcnow()
    
    await ctx.send(embed=embed3)
