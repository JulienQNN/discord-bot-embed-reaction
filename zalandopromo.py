from __future__ import print_function
from asyncio.tasks import wait
import os.path
from discord import member, message
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pickle
import os.path
import base64
from bs4 import BeautifulSoup
from lxml.html.soupparser import fromstring
from lxml.etree import tostring
from discord.ext import commands, tasks
import discord
import random
import json
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
from faker import Faker
import dotenv

"""
logs
"""
logging.basicConfig(filename='MonitoLog.log', filemode='a', format='%(asctime)s - %(name)s - %(message)s',
                    level=logging.DEBUG)
"""
configurations
"""
CONFIG = dotenv.dotenv_values()
TOKEN = CONFIG['DISCORD_TOKEN']

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def randomCode():
        with open("promocode.json", 'r') as f:
         score = json.load(f)
         random_item_from_list = random.choice(score)
         score.remove(random_item_from_list)
        
        print(random_item_from_list)     
        number_of_elements = len(score)
        print(number_of_elements)  
        
        with open("promocode.json", 'w') as f:
         json.dump(score, f)
        return random_item_from_list


client = discord.Client()
intents = discord.Intents.default()
intents.members = True


def discordbot():
        @client.event
        async def on_ready():
            print('We have logged in as {0.user}'.format(client))
            channel = client.get_channel(909524187843035146)
            embed = discord.Embed(
                title='Izi Cookz Code Promo',
                description='Clique sur 🎫 pour recevoir un code Promo de -10% sur le site de Zalando ! ⚠️ Merci de ne pas spam le bot ⚠️ !',
                color=int(CONFIG['COLOUR']))
            embed.set_thumbnail(
            url="https://i.ibb.co/0V6G4qW/zal.png")
            embed.set_footer(text="Made by JLM for Izi Cookz",
                             icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
            msg = await channel.send(embed=embed)
            await msg.add_reaction("🎫")

            
def discordbotReaction():
        @client.event
        async def on_raw_reaction_add(payload):
          if(payload.message_id == 909524187843035146 and payload.emoji.name == "🎫"):  
            msg = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
            member = discord.utils.get(msg.reactions, emoji="🎫")

            user = payload.member
            print(payload)
            message = "[Génération du code]"
            await user.send(message)
            await msg.remove_reaction("🎫", user)
            time.sleep(3)
            message2 = ("Voici ton code : " + randomCode())
            await user.send(message2)
            
 
          if(payload.message_id == 909524187843035146 and payload.emoji.name == "🎟️"):  
            user = payload.member 
            role = discord.utils.find(lambda r: r.name == 'Premium GOLD', user.roles)
            msgGold = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
            if role in user.roles:  
                memberGold = discord.utils.get(msgGold.reactions, emoji="🎟️")
                userGold = payload.member
                print(payload)
                message = "[Génération des codes]"
                await userGold.send(message)
                await msgGold.remove_reaction("🎟️", userGold)
                time.sleep(3)
                i = 0
                waitingMsg = ("Voici tes codes :")
                await userGold.send(waitingMsg)
                while i < 3:
                    Codes = (randomCode())
                    await userGold.send(Codes)
                    i = i+1
            else:
                userGold = payload.member
                
                await userGold.send(":octagonal_sign: Tu n'est pas encore GOLD ! :octagonal_sign:")
            userGold = payload.member
            await msgGold.remove_reaction("🎟️", userGold)
            
          if(payload.message_id == 909524187843035146 and payload.emoji.name == "📇"):  
            user = payload.member
            role = discord.utils.find(lambda r: r.name == 'Premium PLATINE', user.roles)
            msgPLATINE = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
            if role in user.roles:  
                memberPLATINE = discord.utils.get(msgPLATINE.reactions, emoji="📇")
                userPLATINE = payload.member
                print(payload)
                message = "[Génération des codes]"
                await userPLATINE.send(message)
                await msgPLATINE.remove_reaction("📇", userPLATINE)
                time.sleep(3)
                i = 0
                waitingMsg = ("Voici tes codes :")
                await userPLATINE.send(waitingMsg)
                while i < 5:
                        Codes = (randomCode())
                        await userPLATINE.send(Codes)
                        i = i+1
            else:
                userPLATINE = payload.member
                await userPLATINE.send(":octagonal_sign:  Tu n'est pas encore PLATINE :octagonal_sign: ")
            userPLATINE = payload.member
            await msgPLATINE.remove_reaction("📇", userPLATINE)



        TOKEN = CONFIG['DISCORD_TOKEN']
        client.run(TOKEN)

if __name__ == '__main__': 
    discordbotReaction()
        
#def zalandopromo():
#    start = 0
 #   while (start < 1):
  #    print(start)
   #   start = start+1
    #  promoAuto()
     # if start == 1:   
      #          break
      # 


