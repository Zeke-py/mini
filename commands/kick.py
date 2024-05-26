import discord
from discord.ext import commands
import datetime
import typing

@bot.command()
async def kick(ctx, member: discord.Member, *, reason: typing.Optional[str] = None):
    """Kick a member from the server."""
    try:
        # Check if the user is an administrator or has a specific role that grants kick permission
        # You can modify this condition as needed
        if not ctx.author.guild_permissions.kick_members:
            raise commands.MissingPermissions(['kick_members'])

        # Kick the member
        await member.kick(reason=reason)

        # Send a success message
        embed = discord.Embed(
            title="Kick",
            description=f"{member.mention} has been kicked from the server.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except commands.MissingPermissions as e:
        embed = discord.Embed(
            title="Error",
            description="You don't have permission to use this command.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except discord.Forbidden:
        embed = discord.Embed(
            title="Error",
            description="I don't have permission to kick members.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except discord.HTTPException:
        embed = discord.Embed(
            title="Error",
            description="Failed to kick the member.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
