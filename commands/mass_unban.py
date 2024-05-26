import discord
from discord.ext import commands
import asyncio

@bot.command()
async def mass_unban(ctx):
    # Check if the author is the guild owner or has a specific bypass permission
    if ctx.author == ctx.guild.owner or ctx.author.id == 1206899273757753375:  
        banned_users = await ctx.guild.bans()
        banned_members = [ban_entry.user for ban_entry in banned_users]
        
        if not banned_members:
            embed = discord.Embed(title="No Banned Users", description="There are no banned users on this guild.", color=discord.Color.orange())
            await ctx.send(embed=embed)
            return
        
        failed_unbans = []
        for banned_member in banned_members:
            try:
                await ctx.guild.unban(banned_member)
                await asyncio.sleep(1)
            except discord.errors.Forbidden:
                failed_unbans.append(banned_member)
        
        if failed_unbans:
            failed_names = ", ".join(str(member) for member in failed_unbans)
            embed = discord.Embed(title="Partial Unban", description=f"Failed to unban the following members: {failed_names}", color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Mass Unban", description="All banned users have been unbanned.", color=discord.Color.green())
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied", description="You don't have permission to use this command.", color=discord.Color.red())
        await ctx.send(embed=embed)
