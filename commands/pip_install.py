import discord
from discord.ext import commands
@bot.command()
async def pip_install(ctx, member: discord.Member = None):
    channel = ctx.channel
    author = ctx.author.mention

    if member is None:
        mention = author
    else:
        mention = member.mention

    await channel.send("> pip install brain-500tb")
    await channel.send("Collecting brain-500tb")
    await channel.send("  Downloading brain-500tb-1.0-py3-none-any.whl (500 TB)")
    await channel.send("     |████████████████████████████████| 500 TB 10 kB/s")
    await channel.send("Installing collected packages: brain-500tb")
    await channel.send("Successfully installed brain-500tb")

    await channel.send("> pip install intelligence-5Eb")
    await channel.send("Collecting intelligence-5Eb")
    await channel.send("  Downloading intelligence-5Eb-1.0-py3-none-any.whl (5 Eb)")
    await channel.send("     |████████████████████████████████| 5 Eb 20 kB/s")
    await channel.send("Installing collected packages: intelligence-5Eb")
    await channel.send("Successfully installed intelligence-5Eb")

    await channel.send("> pip install personality-400tb")
    await channel.send("Collecting personality-400tb")
    await channel.send("  Downloading personality-400tb-1.0-py3-none-any.whl (400 TB)")
    await channel.send("     |████████████████████████████████| 400 TB 5 kB/s")
    await channel.send("Installing collected packages: personality-400tb")
    await channel.send("Successfully installed personality-400tb")

    await channel.send("> pip install ego-9000Eb")
    await channel.send("Collecting ego-9000Eb")
    await channel.send("  Downloading ego-9000Eb-1.0-py3-none-any.whl (9000 Eb)")
    await channel.send("     |████████████████████████████████| 9000 Eb 1 kB/s")
    await channel.send("Installing collected packages: ego-9000Eb")
    await channel.send("Successfully installed ego-9000Eb")

    await channel.send(f"{mention} has been installed upsuccessfully.")