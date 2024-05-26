import discord
from discord.ext import commands
import os
# Function to log member messages
async def log_member_messages(message):
    server_name = message.guild.name
    member_name = message.author.name
    message_content = f"{message.created_at} | #{message.channel.name} | {message.content}\n"

    server_folder = f"message_database/{server_name}"
    member_file = f"{server_folder}/{member_name}.txt"

    # Create server folder if it doesn't exist
    if not os.path.exists(server_folder):
        os.makedirs(server_folder)

    # Log message in member file
    with open(member_file, 'a') as file:
        file.write(message_content)

# Event triggered when a message is sent
@bot.event
async def on_message(message):
    if not message.author.bot:
        await log_member_messages(message)
    await bot.process_commands(message)