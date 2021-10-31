import discord
from discord import channel
#9/29/2020 made by TekMage
#L30 Key
from discord.ext import commands
import asyncio

import time

from datetime import date
import datetime

from discord.ext.commands.converter import PartialEmojiConverter
from discord.raw_models import RawReactionActionEvent

#Your Discord Bots Token goes here. You can individually put it in every time you need it, but this alos works
TOKEN = ''
   
#Your going to start all of your commands with this
bot = commands.Bot(command_prefix="/")
print('Deployed ReactoR')

#List of channels to look at 
listofsorts = ()

#The Sauccce
@bot.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    
    if user.bot:
        return
                                        #Dummy Paste's examples                                 #Dummy Paste's examples
    if reaction.message.channel.id == int(901379831449649202) or reaction.message.channel.id == int(901379831449649202) :
        if emoji == "💸":

            #Reposts content to a new channel 
            print('Reposting')
            val = (reaction.message.content)
            channel = bot.get_channel(901380502773186601)
            await channel.send(val)
            #Reposts content to a new channel 

    #For testing or just extra I don't remember why this is here
    elif emoji == "🦴":
        print('Bones')
    else:
        return     
  


    

    
#Runs the Bot       
bot.run(TOKEN)
