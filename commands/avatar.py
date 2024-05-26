import discord
from discord.ext import commands
from datetime import datetime

@bot.command(aliases=['av', 'userav'])
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    guild = ctx.guild  

    # Check if the member has an avatar
    if not member.avatar.url == None:
        embed = discord.Embed(
            title=f"{member.name}'s Avatar".capitalize(),
            color=discord.Color.blue(),
        )

        embed.set_author(name=member.name, icon_url=member.avatar.url)
        embed.set_thumbnail(url=guild.icon.url)
        embed.set_image(url=member.avatar.url)
        embed.set_footer(text=f"Requested by | {member.name}", icon_url=member.avatar.url)
        embed.timestamp = datetime.utcnow()

        await ctx.send(embed=embed)
    else:
        await ctx.send(embed = discord.Embed(title = "AVATAR",color=discord.Color.blue() ,description = f"{member.name} doesn't have an avatar."))
