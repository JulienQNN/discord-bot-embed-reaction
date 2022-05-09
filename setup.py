from __future__ import print_function
import discord
from discord.ext import commands
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
        embed=discord.Embed(title=TITLE, timestamp=datetime.now(timezone.utc), description=DESCRIPTION, url=URL, colour=COLOUR)
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_footer(text=FOOTER_DESCRIPTION,icon_url=AVATAR_FOOTER_URL)
        message = await channel.send(embed=embed) 
        await message.add_reaction(TICKET)
        await message.add_reaction(TICKET_TRIPLE)
        await message.add_reaction(TICKET_QUINTUPLE)

# The CHANNEL_ID where the message embed will be sent
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# Adding the intent to True  
intents = discord.Intents.default()
intents.message_content = True

# Running the client with the token of your Bot (From your discord developer portal) 
initialMessage = MyClient(intents=intents)
initialMessage.run(os.getenv("DISCORD_TOKEN"))