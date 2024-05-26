import discord
from discord.ext import commands
import datetime
from datetime import datetime
import random
import os
import asyncio
@bot.command(aliases=['s_name', 'server_name'])
async def servername(ctx, name: str):
    """Edit the name of the guild."""
    try:
        # Check if the user is the owner of the guild
        if ctx.guild.owner != ctx.author:
            raise commands.MissingPermissions(['guild owner'])

        # Edit the name of the guild
        await ctx.guild.edit(name=name)

        # Send a success message
        embed = discord.Embed(
            title="GUILD NAME EDITED",
            description=f"Guild name has been changed to {name}.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    except commands.MissingPermissions as e:
        embed = discord.Embed(
            title="Error",
            description="You must be the owner of the guild to use this command.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except discord.Forbidden:
        embed = discord.Embed(
            title="Error",
            description="I don't have permission to edit the guild's name.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except discord.HTTPException:
        embed = discord.Embed(
            title="Error",
            description="Failed to edit the guild's name.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=str(e),
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
