import discord
from discord.ext import commands
import random
import os
import datetime
import canvacord
import json
import asyncio
from discord.ext.commands import has_permissions
# creation of intance of bot and  setting presence status text
# loading token from env file using dotenv
# Load commands
# Function to load prefix for a guild from file
def load_guild_prefix(guild_id):
    try:
        filename = f"server_prefix/{guild_id}.txt"
        with open(filename, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        # If file not found, create it with default prefix
        save_guild_prefix(guild_id, ",")
        return ","

# Function to save guild prefix to file
def save_guild_prefix(guild_id, prefix):
    filename = f"server_prefix/{guild_id}.txt"
    with open(filename, "w") as f:
        f.write(prefix)

# Function to load default prefix
def load_default_prefix():
    try:
        with open("bot_prefix.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        # If file not found, create it with default prefix
        with open("bot_prefix.txt", "w") as f:
            f.write(",")
        return ","
BOT_TOKEN = os.getenv("BOT_TOKEN")
status_text = 'WATCHING EVERYTHING'
bot = commands.Bot(command_prefix= load_default_prefix() ,intents=discord.Intents.all())
bot.remove_command("help")

# bot online event
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=status_text))
    await bot.tree.sync()
    print(f"{bot.user} is synced successfully")
    print(f'{bot.user} has connected to Discord!')
    
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

# Load events
for filename in os.listdir('./events'):
    if filename.endswith('.py'):
        bot.load_extension(f'events.{filename[:-3]}')
    
# Command to change bot's prefix (owner-only)
@bot.command()
@commands.is_owner()
async def bot_prefix(ctx, new_prefix: str):
    with open("bot_prefix.txt", "w") as f:
        f.write(new_prefix)
    embed = discord.Embed(title="Prefix Changed", description=f"Prefix changed to: {new_prefix}", color=discord.Color.blue())
    await ctx.send(embed=embed)
    print(f"Prefix changed to: {new_prefix}")

# Error handling for prefix command (non-owner)
@bot_prefix.error
async def prefix_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        embed = discord.Embed(title="Permission Denied", description="You do not have permission to change the bot prefix. This command is owner-only.", color=discord.Color.red())
        await ctx.send(embed=embed)


# Command to change guild's prefix (guild-only)
@bot.command(aliases=['prefix'])
@commands.guild_only()
async def serverprefix(ctx, new_prefix: str):
    if ctx.author.guild_permissions.administrator:
        save_guild_prefix(ctx.guild.id, new_prefix)
        embed = discord.Embed(title="Guild Prefix Changed", description=f"Guild prefix changed to: {new_prefix}", color=discord.Color.blue())
        await ctx.send(embed=embed)
        print(f"Guild prefix changed to: {new_prefix}")
    else:
        embed = discord.Embed(title="Permission Denied", description="You do not have permission to change the guild prefix. This command requires administrator permissions.", color=discord.Color.red())
        await ctx.send(embed=embed)


# Override the default prefix function
async def determine_prefix(bot, message):
    guild_prefix = load_guild_prefix(message.guild.id)
    if guild_prefix is not None:
        return commands.when_mentioned_or(guild_prefix)(bot, message)
    else:
        return commands.when_mentioned_or(load_default_prefix())(bot, message)

bot.command_prefix = determine_prefix    

# Command to change bot's status (owner-only)
@bot.command()
@commands.is_owner()
async def changestatus(ctx, status_type: str, *, status_text: str):
    status_type = status_type.lower()
    embed = discord.Embed(color=discord.Color.blue())
    if changestatus == None and status_text == None:
        embed.add_field(name="Status Change", value="command usage\n<prefix>changestatus <status_type(dnd,online etc)> <status_text(anything)>")
    elif status_type == "playing":
        await bot.change_presence(activity=discord.Game(name=status_text))
        embed.add_field(name="Status Changed", value=f"Status changed to: Playing {status_text}")
    elif status_type == "streaming":
        await bot.change_presence(activity=discord.Streaming(name=status_text, url="twitch_url"))
        embed.add_field(name="Status Changed", value=f"Status changed to: Streaming {status_text}")
    elif status_type == "listening":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status_text))
        embed.add_field(name="Status Changed", value=f"Status changed to: Listening to {status_text}")
    elif status_type == "watching":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status_text))
        embed.add_field(name="Status Changed", value=f"Status changed to: Watching {status_text}")
    elif status_type == "competing":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=status_text))
        embed.add_field(name="Status Changed", value=f"Status changed to: Competing in {status_text}")
    elif status_type == "dnd":
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=status_text))
        embed.add_field(name="Status Changed", value=f"Status changed to: Do Not Disturb, Playing {status_text}")
    elif status_type == "idle":
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=status_text))
        embed.add_field(name="Status Changed", value=f"Status changed to: Idle, Playing {status_text}")
    elif status_type == "online":
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=status_text))
        embed.add_field(name="Status Changed", value=f"Status changed to: Online, Playing {status_text}")
    elif status_type == "offline":
        await bot.change_presence(status=discord.Status.offline)
        embed.add_field(name="Status Changed", value="Status changed to: Offline")
    else:
        embed.add_field(name="Invalid Status Type", value="Invalid status type. Available types: playing, streaming, listening, watching, competing, dnd, idle, online, offline")
    
    await ctx.send(embed=embed)

# Error handling for changestatus command (non-owner)
@changestatus.error
async def changestatus_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        embed = discord.Embed(title="Permission Denied", description="You do not have permission to change the bot status. This command is owner-only.", color=discord.Color.red())
        await ctx.send(embed=embed)


@bot.command()
async def hello(ctx):
    embed = discord.Embed(title="Hello!", description="Hello, world!", color=discord.Color.blue())
    await ctx.send(embed=embed)

bot.run(BOT_TOKEN)