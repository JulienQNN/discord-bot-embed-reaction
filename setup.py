import discord
import os
from helpers import *
from dotenv import load_dotenv
from datetime import datetime, timezone

# Loading environment variables
os.system("")
load_dotenv()

# This will set-up the message embed     
class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(CHANNEL_ID)
        embed=discord.Embed(title=TITLE, timestamp=datetime.now(timezone.utc), description=DESCRIPTION_SETUP, url=URL_SETUP, colour=COLOUR_SETUP)
        embed.set_thumbnail(url=THUMBNAIL_SETUP)
        embed.set_footer(text=FOOTER_DESCRIPTION_SETUP,icon_url=AVATAR_FOOTER_URL_SETUP)
        message = await channel.send(embed=embed) 
        await message.add_reaction(REACTION_1)
        await message.add_reaction(REACTION_2)
        await message.add_reaction(REACTION_3)

# The CHANNEL_ID where the message embed will be sent
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# Adding the intent to True  
intents = discord.Intents.default()
intents.message_content = True

# Running the client with the token of your Bot (From your discord developer portal) 
initialMessage = MyClient(intents=intents)
initialMessage.run(os.getenv("DISCORD_TOKEN"))