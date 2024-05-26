import discord
from discord.ext import commands
@bot.command(name='embed', description='Create an embed using the specified parameters.')
async def create_embed(ctx, *, args):
    # Split the input arguments using "|"
    elements = args.split('|')

    # Trim any leading or trailing spaces from each element
    elements = [element.strip() for element in elements]

    # Set default values in case optional elements are not provided
    title = elements[0] if elements else "No Title"
    description = elements[1] if len(elements) > 1 else "No Description"
    thumbnail_url = elements[2] if len(elements) > 2 else None
    image_url = elements[3] if len(elements) > 3 else None
    footer_text = elements[4] if len(elements) > 4 else None

    # Create the embed
    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Color.blue()
    )
    if thumbnail_url:
        embed.set_thumbnail(url=thumbnail_url)
    if image_url:
        embed.set_image(url=image_url)
    if footer_text:
        embed.set_footer(text=footer_text, icon_url=ctx.author.avatar.url)
    else:
        embed.set_footer(icon_url=ctx.author.avatar.url)

    # Set timestamp in footer
    embed.timestamp = ctx.message.created_at

    # Send the embed
    await ctx.send(embed=embed)

