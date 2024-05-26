# Import necessary libraries
import discord
from discord.ext import commands
import datetime
import asyncio

# Define the ban command
@bot.command(aliases=['destroy', 'shadow_realm'])
async def ban(ctx, member: discord.Member = None, *, reason=None):
    """Ban a member from the server."""
    try:
        if member is None:
            raise commands.MissingRequiredArgument

        if not ctx.author.guild_permissions.administrator:
            raise commands.MissingPermissions(['administrator'])

        if ctx.author.top_role <= member.top_role:
            raise commands.BadArgument("You can't ban members with equal or higher role!")

        await member.ban(reason=reason)
        
        # Create the embed
        embed = discord.Embed(
            title="BAN",
            description=f'{member} has been banned from the server.',
            color=discord.Color.red()
        )
        
        # Set footer with timestamp and requester's name
        embed.set_footer(
            text=f"Requested by {ctx.author.name}",
            icon_url=ctx.author.avatar.url
        )
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)

    except commands.MissingRequiredArgument:
        await ctx.send(embed=discord.Embed(title="BAN", description="Please mention a member to ban.", color=discord.Color.red()))

    except commands.MissingPermissions as e:
        await ctx.send(embed=discord.Embed(title="BAN", description="You don't have permission to use this command.", color=discord.Color.red()))

    except commands.BadArgument as e:
        await ctx.send(embed=discord.Embed(title="BAN", description=str(e), color=discord.Color.red()))

    except discord.NotFound:
        await ctx.send(embed=discord.Embed(title="BAN", description="Member not found.", color=discord.Color.red()))

    except discord.Forbidden:
        await ctx.send(embed=discord.Embed(title="BAN", description="I don't have permission to ban members.", color=discord.Color.red()))

    except discord.HTTPException:
        await ctx.send(embed=discord.Embed(title="BAN", description="Failed to ban the member.", color=discord.Color.red()))
