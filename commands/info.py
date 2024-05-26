import discord
from discord.ext import commands
import datetime

@bot.command(aliases=['memberinfo', 'information', 'details'])
async def info(ctx, member: discord.Member = None):
    member = member or ctx.author
    guild = ctx.guild

    try:
        # Get the member's roles as a string
        roles = ", ".join([role.name for role in member.roles[1:]])  # Exclude @everyone role

        # Get the member's permissions as a string
        permissions = "\n".join([f"{perm[0].replace('_', ' ').title()}: {perm[1]}" for perm in member.guild_permissions if perm[1]])

        # Get total number of human members, bots, and emojis on the server
        total_human_members = sum(not member.bot for member in guild.members)
        total_bots = sum(member.bot for member in guild.members)
        total_emojis = len(guild.emojis)

        # Get total number of text and voice channels
        total_text_channels = len(guild.text_channels)
        total_voice_channels = len(guild.voice_channels)

        # Check if the member has a banner
        banner_url = member.banner.url if member.banner else None

        # Create the embed message
        embed = discord.Embed(
            title=f"{member.name}'s Information",
            color=discord.Color.blue(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="User ID", value=member.id, inline=False)
        embed.add_field(name="Nickname", value=member.display_name, inline=False)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%b %d, %Y %H:%M:%S"), inline=False)
        embed.add_field(name="Joined Discord", value=member.created_at.strftime("%b %d, %Y %H:%M:%S"), inline=False)
        if roles:
            embed.add_field(name="Roles", value=roles or "None", inline=False)
        if permissions:
            embed.add_field(name="Permissions", value=permissions, inline=False)
        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="Server ID", value=guild.id, inline=False)
        embed.add_field(name="Server Owner", value=guild.owner.display_name, inline=False)
        embed.add_field(name="Server Creation Time", value=guild.created_at.strftime("%b %d, %Y %H:%M:%S"), inline=False)
        embed.add_field(name="Counter", value=f"Total Human: {total_human_members}\nTotal Bots: {total_bots}\nTotal Emojis: {total_emojis}\nTotal Text Channels: {total_text_channels}\nTotal Voice Channels: {total_voice_channels}", inline=False)
        if banner_url:
            embed.set_image(url=banner_url)
        embed.set_footer(text=f"Requested by | {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)

    except discord.HTTPException:
        await ctx.send(embed=discord.Embed(
            title="Error",
            description="Failed to retrieve member information.",
            color=discord.Color.red()
        ))

    except Exception as e:
        await ctx.send(embed=discord.Embed(
            title="Error",
            description=str(e),
            color=discord.Color.red()
        ))
