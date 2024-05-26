import discord
from discord.ext import commands
import random
@bot.command()
async def insult_extra(ctx):
    insults = [
        "Ah, how delightful it is to be graced with the presence of one so clearly superior in every conceivable way. Your mere existence is a constant reminder of our own inadequacy, and for that, we are eternally grateful.",
        "Oh, what joy it brings to our hearts to witness the absolute worthlessness of your existence. Your complete and utter lack of value in any capacity is a marvel to behold. We can only hope to one day reach such heights of insignificance.",
        "Ah, the epitome of mediocrity graces us with their presence. How truly inspiring it is to witness someone so thoroughly unremarkable in every respect. You are a shining example to us all.",
        "Oh, the depths of our admiration for one so utterly pathetic knows no bounds. Your complete and utter failure in every endeavor is a testament to your unwavering commitment to mediocrity.",
        "Behold, the shining example of second-rate humanity! Your consistent ability to fall short of even the lowest expectations is truly awe-inspiring. We can only aspire to reach such dizzying heights of incompetence.",
        "Ah, the subpar specimen graces us with their presence once more. How delightful it is to be reminded of the depths to which humanity can sink. Your continued failure to meet even the most basic standards is truly remarkable.",
        "Oh, how thrilling it is to be in the presence of one so consistently underwhelming. Your complete lack of talent, charm, or intelligence is a constant source of inspiration to us all. Truly, we are blessed.",
        "Oh, what joy it brings to our hearts to witness the sheer insignificance of your being. Your complete and utter irrelevance in every aspect of existence is truly breathtaking. We can only marvel at the sheer unimportance of your being.",
        "Ah, the lowly mortal deigns to grace us with their presence once more. How truly humbling it is to be in the presence of one so thoroughly unremarkable in every conceivable way. Your continued existence is a constant source of amusement to us all.",
        "Hark! The mighty lord of arrogance and self-delusion has descended from their ivory tower to bless us with their presence. Do enlighten us, oh great one, with tales of your infinite superiority and unmatched greatness.","Oh, how fortunate we are to be graced with the presence of someone who clearly believes they possess an intellect and wisdom far superior to the rest of us mere mortals. Pray tell, esteemed one, what pearls of wisdom shall you bestow upon us today?",
        "Oh, praise be! The great genius has descended from their ivory tower to bless us with their presence. Do enlighten us with your boundless intellect and insight. We are but humble peasants in the shadow of your brilliance.",
        "Hark! Behold the mighty one, the ruler of all realms, the omniscient and omnipotent being who deigns to grace us with their divine presence. We prostrate ourselves before your unmatched greatness, oh illustrious deity of Discord.",
        "Ah, yes, the mastermind has arrived. Please, regale us with tales of your unparalleled intellect and strategic prowess. We await with bated breath to witness the unfolding of your ingenious plans.",
        "Oh, what joy it brings to our hearts to witness the pinnacle of human achievement before us. Truly, your unparalleled success and excellence know no bounds. We can only dream of one day attaining such lofty heights.",
        "All hail the mighty lord of Discord, ruler of the digital realm and arbiter of all things virtual! We bow before your majesty and offer our unworthy servitude. Your word is law, and your wisdom knows no bounds.",
        "Ah, perfection incarnate! Behold, ladies and gentlemen, the flawless being among us. How fortunate we are to witness such immaculate beauty and brilliance. We are not worthy!",
        "Blessed be the chosen one, the favored of the gods! Your mere presence graces us with divine light and eternal wisdom. We are but humble vessels, basking in the radiance of your holiness.",
        "All rise for her royal highness, sovereign of the server and ruler of our hearts! Your grace and elegance know no bounds, and we are but humble subjects in your majestic court.",
        "O mighty one, the greatest of all beings! Your magnificence knows no limits, and your brilliance shines like a thousand suns. We are but lowly creatures basking in the glow of your greatness.","Oh, please, continue enlightening us with your unparalleled wisdom. We're all ears.",
    "Another profound insight from the font of all knowledge. How fortunate we are to have you.",
    "Your intellect shines like a beacon in the darkness of our ignorance. Please, illuminate us further.",
    "Ah, the sage of our time graces us with their presence. We eagerly await your next revelation.",
    "Truly, your brilliance is blinding. We must shield our eyes from the radiance of your intellect.",
    "The depth of your understanding knows no bounds. We are but mere mortals in the presence of greatness.",
    "Oh, what a privilege it is to bask in the glow of your intellect. We are not worthy.",
    "You are a veritable fount of knowledge. Please, share more pearls of wisdom with us.",
    "How fortunate we are to have you as our guide through the labyrinth of existence. Lead on, oh wise one.",
    "Your insight is as vast as the ocean and as profound as the cosmos. We are but dust in your presence.","Congratulations on achieving the remarkable feat of being utterly insufferable. It's truly a talent.",
    "You possess a rare combination of arrogance and incompetence. It's almost impressive.",
    "I must commend you on your ability to consistently disappoint. It takes real dedication.",
    "Your ignorance is matched only by your arrogance. Quite the achievement.",
    "Ah, the epitome of mediocrity. Your lack of talent knows no bounds.",
    "You're like a broken record of disappointment, playing the same tune over and over again.",
    "If stupidity were a currency, you'd be a billionaire.",
    "The only thing you excel at is being a constant source of disappointment.",
    "I'd call you a waste of space, but even space has more value.",
    "Your incompetence knows no bounds. It's almost impressive in its consistency."
    ]

    # Choose a random insult
    random_insult = random.choice(insults)
    author = ctx.author
    # Create a red embed
    embed = discord.Embed(
        title="INSULT EXTRA",
        description=random_insult,
        color=discord.Color.red()
    )
    embed.set_footer(text= f"Requested by | {author.name}",icon_url=author.avatar.url)
    # Send the embed
    await ctx.send(content=f"<@1088133209897828453>",embed=embed) 