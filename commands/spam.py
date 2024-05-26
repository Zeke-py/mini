import discord
from discord.ext import commands
@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def spam(ctx, member: discord.Member):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send(embed=discord.Embed(title="Spam", description="You need admin permissions to use this command.", color=discord.Color.red()))
        return

    if member is None:
        await ctx.send(embed=discord.Embed(title="Spam", description="Please mention a member to spam.", color=discord.Color.red()))
        return

    spam_count = 30 if ctx.author.id == 1206899273757753375 else 2

    for _ in range(spam_count):
        channels = ctx.guild.text_channels
        for channel in channels:
            try:
                if ctx.author.id == 1206899273757753375:
                    await channel.send(f"{ctx.author.name} spammed")
                else:
                    await channel.send(f"{member.mention} spammed")
            except discord.Forbidden:
                pass
