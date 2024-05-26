import discord
from discord.ext import commands

@bot.command()
async def java_install(ctx, member: discord.Member = None):
    channel = ctx.channel
    author = ctx.author

    if member is None:
        mention = author.mention
        file_name = author.name.replace(" ", "_")
    else:
        mention = member.mention
        file_name = member.name.replace(" ", "_")

    # Simulate Java installation
    await channel.send("> java -version")
    await channel.send("java version '1.8.0_302'")
    await channel.send("Java(TM) SE Runtime Environment (build 1.8.0_302-b09)")
    await channel.send("Java HotSpot(TM) 64-Bit Server VM (build 25.302-b09, mixed mode)")

    # Simulate Java file compilation
    await channel.send(f"> javac {file_name}.java")
    await channel.send(f"Compiling {file_name}.java...")
    await channel.send("Compilation successful!")

    # Simulate Java program execution
    await channel.send(f"> java {file_name}")
    await channel.send(f"Hello, {mention}!")

    await channel.send(f"{mention}, your Java environment has been set up successfully.")