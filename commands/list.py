import discord
from discord.ext import commands
import datetime
import asyncio

@bot.command(aliases=['member_list'])
async def list(ctx):
    await ctx.message.delete()

    # Get the list of members in the server
    members = ctx.guild.members
    member_list = [f"{member.name} {member.display_name} ({member.id}) " for member in members]

    # Pagination variables
    current_page = 0
    page_size = 10

    # Function to create embed for current page
    def create_embed():
        start_index = current_page * page_size
        end_index = min((current_page + 1) * page_size, len(member_list))
        current_members = member_list[start_index:end_index]

        # Format member list with bullets
        member_info = "\n".join(current_members)

        embed = discord.Embed(title=f"Member List - Page {current_page + 1}/{len(member_list) // page_size + 1}",
                              description=f"```{member_info}```",
                              color=discord.Color.blue())
        
        # Add information about who requested the command
        embed.set_footer(text=f"Requested by {ctx.author.name} | {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}",
                         icon_url=ctx.author.avatar.url)

        return embed

    # Send initial embed
    message = await ctx.send(embed=create_embed())

    # Add reactions
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    # Reaction check
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)

            if str(reaction.emoji) == "◀️" and current_page > 0:
                current_page -= 1
                await message.edit(embed=create_embed())
            elif str(reaction.emoji) == "▶️" and current_page < len(member_list) // page_size:
                current_page += 1
                await message.edit(embed=create_embed())

            await message.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            break
