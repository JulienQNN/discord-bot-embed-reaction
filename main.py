import discord
import os
import random
from helpers import *
import json
from dotenv import load_dotenv
from datetime import datetime, timezone

# Loading environment variables
os.system("")
load_dotenv()

# The main class                            
class MyClient(discord.Client):
    
    # Check if discord client is started and print it
    async def on_ready(self):
        print('Logged on as', self.user)

    # The function that permit your bot to listen every message reaction mades on your server(s)
    async def on_raw_reaction_add(self, payload): 
        
        # payload will give info's of the discord member who add a reaction
        user = payload.member
        pld_channId = payload.channel_id
        pld_messId = payload.message_id
        emoji = payload.emoji.name
        userRoles = payload.member.roles
        
        # the discord message u want to listen for reactions added 
        msg = await client.get_channel(pld_channId).fetch_message(pld_messId)
        
        # the discord button on all embeds sent in private message by the bot to users
        view=Buttons().add_item(discord.ui.Button(label="YOUR LINK TITLE",style=discord.ButtonStyle.link,url=URL, emoji=BUTTON_LINK_EMOJI))
        
        # the user roles to use the second and third reaction of the embed
        role1 = discord.utils.find(lambda r: r.name == ROLE1, userRoles)
        role2 = discord.utils.find(lambda r: r.name == ROLE2, userRoles)
        
        # the embed model using parameters: timestamp, colour, thumbnail, footer description, avatar footer url
        embed=discord.Embed(timestamp=datetime.now(timezone.utc), colour=COLOUR)
        embed.set_thumbnail(url=THUMBNAIL)
        embed.set_footer(text=FOOTER_DESCRIPTION, icon_url=AVATAR_FOOTER_URL)
           
        # check if the channel_id of the payload reaction added is the same that u choosed in your "helpers.py" file and there is stil vouchers in the vouchers.json file
        if pld_messId == client.message_or_embed_id and VoucherFileCheker(user, view) == 1:       
            
                    # check if the reaction emoji added is the same as your TICKET emoji added in your "helpers.py" file
                    if  emoji == TICKET:
                        await msg.remove_reaction(TICKET, user)          
                        embed.add_field(name="YOUR FIELD TITLE", value=VoucherPicker(1), inline=True)
                        
                    # check if the reaction emoji added is the same as your TICKET_TRIPLE emoji added in your "helpers.py" file
                    if emoji == TICKET_TRIPLE:
                        await msg.remove_reaction(TICKET_TRIPLE, user)
                        
                        # check if one of the roles of the user who added the reaction is the same as ROLE1 that u choosed in your "helpers.py" file, if not it will send a warning
                        if role1 in userRoles:
                            embed.add_field(name="YOUR FIELD TITLE", value=VoucherPicker(3), inline=True)
                        else:
                            embed.add_field(name=WARNING1, value=WARNING1, inline=True)
                            
                    # check if the reaction emoji added is the same as your TICKET_QUINTUPLE emoji added in your "helpers.py" file
                    if emoji == TICKET_QUINTUPLE:
                        await msg.remove_reaction(TICKET_QUINTUPLE, user)
                        
                        # check if one of the roles of the user who added the reaction is the same as ROLE2 that u choosed in your "helpers.py" file, if not it will send a warning
                        if role2 in userRoles:
                            embed.add_field(name="YOUR FIELD TITLE", value=VoucherPicker(5), inline=True)
                        else:
                            embed.add_field(name=WARNING2, value=WARNING2, inline=True) 
                    await user.send(embed=embed, view=view)
                    
        # check if there is atleast 5 vouchers in the vouchers.json file
        if VoucherFileCheker(user, view) == 2:
            # the empty voucher embed model using parameters, u need to re init it to prevent sending again the last vouchers
            embed=discord.Embed(title="NO MORE VOUCHERS TITLE !", description=DESCRIPTION_EMPTY_FILE, timestamp=datetime.now(timezone.utc), colour=COLOUR) 
            embed.set_footer(text=FOOTER_DESCRIPTION, icon_url=AVATAR_FOOTER_URL)
            embed.set_thumbnail(url=THUMBNAIL)
            await msg.remove_reaction(payload.emoji.name, user) 
            await user.send(embed=embed, view=view)        

# The Button Class for every webhook sent to users, u can personalise the redirection link in the "discordbotReaction" function              
class Buttons(discord.ui.View):
            def __init__(self, *, timeout=1800):
                super().__init__(timeout=timeout)

# The function that picks codes at random from the file vouchers            
def VoucherPicker(x):
    # prevent to sent multiple times the same voucher
    available_voucher = []
    
    # open the vouchers file on read mode and pick up codes
    with open(VOUCHER, 'r') as f:
        voucherFile = json.load(f)
        
        for _ in range(x):
            random_voucher_from_list = random.choice(voucherFile)
            voucherFile.remove(random_voucher_from_list)
            available_voucher.append(random_voucher_from_list) 
                
            # open the vouchers file on write mode delete code picked up
            with open(VOUCHER, 'w') as f:
                json.dump(voucherFile, f)

        voucher = '\n'.join(available_voucher)
    return voucher

# The function that check how many vouchers there is in the vouchers.json file
def VoucherFileCheker(user, view):
    with open(VOUCHER, 'r') as f:
        voucherFile = json.load(f)
        if len(voucherFile) > 4:
            return 1
        return 2

# Adding the intent to True    
intents = discord.Intents.default()
intents.message_content = True

# Running the client with the token of your Bot (From your discord developer portal) 
client = MyClient(intents=intents)
client.message_or_embed_id = int(os.getenv("MESSAGE_ID"))
client.run(os.getenv("DISCORD_TOKEN"))