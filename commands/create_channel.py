import discord
from discord.ext import commands

@bot.command(aliases=['channel_create', 'chcrt'])
async def create_channel(ctx, channel_name: str):
    try:
        # Check if the user is an administrator
        if not ctx.author.guild_permissions.administrator:
            raise commands.MissingPermissions(['administrator'])

        # Check if the bot has permission to manage channels
        if not ctx.guild.me.guild_permissions.manage_channels:
            raise discord.Forbidden

        # Create the channel
        new_channel = await ctx.guild.create_text_channel(channel_name)

        # Send a success message with a footer
        embed = discord.Embed(
            title="Success",
            description=f"Channel `{new_channel.name}` created successfully!",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url))

    except commands.MissingPermissions:
        await ctx.send(embed=discord.Embed(
            title="Error",
            description="You need to be an administrator to create channels.",
            color=discord.Color.red()
        ))

    except discord.Forbidden:
        await ctx.send(embed=discord.Embed(
            title="Error",
            description="I don't have permission to create channels.",
            color=discord.Color.red()
        ))

    except discord.HTTPException:
        await ctx.send(embed=discord.Embed(
            title="Error",
            description="Failed to create the channel.",
            color=discord.Color.red()
        ))

    except Exception as e:
        await ctx.send(embed=discord.Embed(
            title="Error",
            description=str(e),
            color=discord.Color.red()
        ))
