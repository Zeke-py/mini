import discord
from discord.ext import commands
import datetime
import random
import os
import asyncio
import json

@client.command()
async def mute(ctx, member: discord.Member, duration: typing.Optional[int] = None, *, reason: typing.Optional[str] = None):
    """Mute a member in the server."""
    try:
        # Check if the user is an administrator or has a specific role that grants mute permission
        if not ctx.author.guild_permissions.manage_roles:
            raise commands.MissingPermissions(['manage_roles'])

        # Fetch or create the mute role
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            mute_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, send_messages=False)

        # Add the mute role to the member
        await member.add_roles(mute_role, reason=reason)

        # Send a success message
        embed = discord.Embed(
            title="Mute",
            description=f"{member.mention} has been muted.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

        # Remove the mute role after the specified duration (if provided)
        if duration:
            await asyncio.sleep(duration)
            await member.remove_roles(mute_role, reason="Mute duration expired")

            # Update mute settings in JSON
            update_mute_settings(member.id, ctx.guild.id, None)

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
            description="I don't have permission to manage roles.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    except discord.HTTPException:
        embed = discord.Embed(
            title="Error",
            description="Failed to perform the mute operation.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

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

# Update mute settings in JSON
def update_mute_settings(member_id, guild_id, duration):
    mute_settings = load_mute_settings()
    mute_settings.setdefault(str(guild_id), {})
    mute_settings[str(guild_id)][str(member_id)] = duration
    save_mute_settings(mute_settings)

# Check mute durations and remove muted role if duration has expired
async def check_mute_durations():
    current_time = datetime.datetime.utcnow()
    mute_settings = load_mute_settings()

    for guild_id, members in mute_settings.items():
        guild = client.get_guild(int(guild_id))
        if guild:
            for member_id, mute_duration in members.items():
                mute_duration = datetime.datetime.fromisoformat(mute_duration)
                if mute_duration <= current_time:
                    member = guild.get_member(int(member_id))
                    if member:
                        mute_role = discord.utils.get(guild.roles, name="Muted")
                        if mute_role:
                            await member.remove_roles(mute_role, reason="Mute duration expired")
                        del mute_settings[guild_id][member_id]

    save_mute_settings(mute_settings)


# Event: Bot initialization
@client.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    # Start a background task to check mute durations
    client.loop.create_task(check_mute_durations())