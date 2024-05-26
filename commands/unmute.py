
import discord
from discord.ext import commands
import datetime
import random
import os
import asyncio
import json

@bot.command()
async def unmute(ctx, member: discord.Member):
    """Unmute a member in the server."""
    try:
        # Check if the user is an administrator or has a specific role that grants unmute permission
        if not ctx.author.guild_permissions.manage_roles:
            raise commands.MissingPermissions(['manage_roles'])

        # Fetch the mute role
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            raise commands.BadArgument("Muted role not found.")

        # Remove the mute role from the member
        await member.remove_roles(mute_role, reason="Unmuted by moderator")

        # Send a success message
        embed = discord.Embed(
            title="Unmute",
            description=f"{member.mention} has been unmuted.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

        # Remove data associated with the member from the mute settings JSON file
        remove_mute_data(member.id, ctx.guild.id)

    except commands.MissingPermissions as e:
        embed = discord.Embed(
            title="Error",
            description="You don't have permission to use this command.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except commands.BadArgument as e:
        embed = discord.Embed(
            title="Error",
            description=str(e),
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except discord.Forbidden:
        embed = discord.Embed(
            title="Error",
            description="I don't have permission to manage roles.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except discord.HTTPException:
        embed = discord.Embed(
            title="Error",
            description="Failed to perform the unmute operation.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

# Remove data associated with the member from the mute settings JSON file
def remove_mute_data(member_id, guild_id):
    mute_settings = load_mute_settings()
    if str(guild_id) in mute_settings and str(member_id) in mute_settings[str(guild_id)]:
        del mute_settings[str(guild_id)][str(member_id)]
        save_mute_settings(mute_settings)

# Load mute settings from mute_settings.json
def load_mute_settings():
    try:
        with open('mute_settings.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save mute settings to mute_settings.json
def save_mute_settings(mute_settings):
    with open('mute_settings.json', 'w') as file:
        json.dump(mute_settings, file, indent=4)