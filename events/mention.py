import discord
from discord.ext import commands
import os

# Function to load prefix for a guild from file
def load_guild_prefixs(guild_id):
    try:
        filename = f"server_prefix/{guild_id}.txt"
        with open(filename, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        # If file not found, return None
        return None

# Function to load default prefix
def load_default_prefixs():
    try:
        with open("bot_prefix.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        # If file not found, create it with default prefix
        with open("bot_prefix.txt", "w") as f:
            f.write(",")
        return ","

# Override the default prefix function
async def determine_prefixs(client, message):
    guild_prefix = load_guild_prefixs(message.guild.id)
    if guild_prefix is not None:
        return commands.when_mentioned_or(guild_prefix)(client, message)
    else:
        return commands.when_mentioned_or(load_default_prefixs())(client, message)

async def on_message(message):
    if message.author.bot:
        return

    if bot.user.mentioned_in(message):
        guild_prefix = load_guild_prefix(message.guild.id)
        if guild_prefix is not None:
            prefix_info = f"My prefix is `{load_default_prefix()}`. Server prefix is `{guild_prefix}`. You can change the server prefix with `{guild_prefix}serverprefix <new_prefix>`."
        else:
            prefix_info = f"My prefix is `{load_default_prefix()}`."
        
        await message.channel.send(prefix_info)

    await bot.process_commands(message)
