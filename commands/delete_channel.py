import discord
from discord.ext import commands

@bot.command(aliases=['channel_delete', 'chdel'])
async def delete_channel(ctx, channel: discord.TextChannel = None):
    if channel is None:
        channel = ctx.channel

    # Check if the user is an administrator
    if not ctx.author.guild_permissions.administrator:
        await ctx.send(embed=discord.Embed(
            title="Error",
            description="You need to be an administrator to use this command.",
            color=discord.Color.red()
        ))
        return

    # Check if the bot has permission to manage channels
    if not ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send(embed=discord.Embed(
            title="Error",
            description="I don't have permission to manage channels.",
            color=discord.Color.red()
        ))
        return

    try:
        # Delete the channel
        await channel.delete()
        
        # Send confirmation message
        await ctx.send(embed=discord.Embed(
            title="Channel Deleted",
            description=f"Channel {channel.mention} has been deleted.",
            color=discord.Color.green()
        ), delete_after=10)
    
    except discord.Forbidden:
        # If the bot lacks permissions to delete the channel
        await ctx.send(embed=discord.Embed(
            title="Error",
            description="I don't have permission to delete that channel.",
            color=discord.Color.red()
        ))

    except discord.HTTPException:
        # If an error occurs during the deletion process
        await ctx.send(embed=discord.Embed(
            title="Error",
            description="An error occurred while trying to delete the channel.",
            color=discord.Color.red()
        ))
