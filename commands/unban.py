import discord
from discord.ext import commands

@bot.command(aliases=['summon', 'call_back'])
async def unban(ctx, member: discord.User = None, *, reason=None):
    """Unban a member from the server."""
    try:
        if member is None:
            raise commands.MissingRequiredArgument

        # Unban the member
        await ctx.guild.unban(member, reason=reason)

        # Send a success message
        embed = discord.Embed(
            title="UNBAN",
            description=f"{member} has been unbanned from the server.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    except commands.MissingRequiredArgument:
        embed = discord.Embed(
            title="UNBAN",
            description="Please specify a user to unban.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except commands.BadArgument as e:
        embed = discord.Embed(
            title="UNBAN",
            description=str(e),
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except discord.Forbidden:
        embed = discord.Embed(
            title="UNBAN",
            description="I don't have permission to unban members.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except discord.HTTPException:
        embed = discord.Embed(
            title="UNBAN",
            description="Failed to unban the member.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
