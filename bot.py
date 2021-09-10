# NoMoreReposti

import os
import random
import re

import reposti
import uwu
import thank
import ggs

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from nltk.corpus import words

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
EightBallList = ['Reply hazy, try again later.',
             'Seems plausible.',
             'Outlook bleak.',
             'Most definitely.',
             'Hard to say.',
             'Utterly impossible.',
             'ur mom TRIPLE gay',
             'More than likely.',
             'Doubtful, but possible.',
             'Eons could pass before such a thing is true.']

deezList = [' deez nuts',
            ' my dick',
            ' in your mouth']
    

opt = Options()
opt.add_argument("--headless")

@client.event
async def on_ready():
    
    print(f'{client.user} has connected to Discord!') # Lets me know this fucker is working.

@client.event
async def on_guild_join(guild): # Creates a text file to manage links on server join.
    
    f = open(f'{guild.name} linkList.txt', 'x')
    f.close()
    f = open(f'{guild.name} linkList.txt', 'w')
    f.write("My hovercraft is full of eels.\n")
    f.close()
    print("Link list for server \"" + guild.name + "\" created successfully.")

@client.event
async def on_message(message):    

    if message.author.bot: # Ignores bot messages.
        return
   
    if '!reposti' in message.content.lower(): # Ignore messages with "!reposti".
        return

    elif '!thepour' in message.content.lower():
        await message.channel.send(file=discord.File('ThePour.jpg'))
        await message.channel.send(
            f'Never forget.'
            )
        return

    elif 'thanks' in message.content.lower(): # Checks for various 'thank-you' messages and replies to them.
        if 'bot' in message.content.lower():
            await message.channel.send(
                f'YOU\'RE WELCOME <@{message.author.id}>'
                )
            return
        elif 'reposti' in message.content.lower():
            await message.channel.send(
                f'YOU\'RE WELCOME <@{message.author.id}>'
                )
            return
        return

    elif 'thank you' in message.content.lower():
        if 'bot' in message.content.lower():
            await message.channel.send(
                f'YOU\'RE WELCOME <@{message.author.id}>'
                )
            return
        elif 'reposti' in message.content.lower():    
            await message.channel.send(
                f'YOU\'RE WELCOME <@{message.author.id}>'
                )
            return
        return

    elif 'nice repost' in message.content.lower():
        await message.channel.send(
            f'Yeah, nice repost.'
            )
        return

    elif '<@!781249441222230076> bitch' in message.content:
        await message.channel.send(
            f'<:okuumug:425764517524537355> \U0001F52B <:Reposti:781288738843656222> You say sumn?'
            )
        return

    elif 'just ' in message.content.lower():
        discordMessage = message.content.lower()
        splitList = discordMessage.split(sep=' ')
        if 'just' in splitList[0]:
            justRand = random.randint(0,79)
            print(
                'Bot rolled a ' + str(justRand) + ', "' + message.content + '"'
                )            
            if justRand == 0:
                await message.channel.send(
                    f'YEAH ' + message.content.upper() + ' LOL'
                )
                return
            else:
                return
    elif 'why ' in message.content.lower():
        discordMessage = message.content.lower()
        splitList = discordMessage.split(sep=' ')
        if 'why' in splitList[0]:
            whyRand = random.randint(0,34)
            print(
                'Bot rolled a ' + str(whyRand) + ', "' + message.content + '"'
                )            
            if whyRand == 0:
                await message.channel.send(
                    f'Why not?'
                )
                return
            else:
                return

    elif message.content.lower() == 'ggs':
        if random.randint(0,8) == 0:
            await message.channel.send(ggs.ggs())
            print('Bot said ggs.')
            return

    elif '!thank' in message.content.lower():
        discordMessage = message.content.lower()
        if thank.thank(discordMessage):
            await message.channel.send(
                    f'fuck you <@{message.author.id}>'                    
                    )        
        else:
            thankMsg = discordMessage.split(sep='!thank ')
            await message.channel.send(f'fuck you ' + thankMsg[1])
        print('Bot "thanked" someone.')
        return

    elif '!8ball' in message.content.lower():
        await message.channel.send(EightBallList[random.randint(0,(len(EightBallList))-1)])
        print('Bot told someone\'s bullshit fortune.')
        return

    elif '!internettime' in message.content.lower():
        await message.channel.send("Let me see...")
        driver = Firefox(options=opt)
        driver.get('http://www.swatchclock.com/')
        html = driver.page_source[1691:1698].split(sep="<")        
        await message.channel.send("It is currently @" + html[0] + ".")
        driver.quit()
        print("Bot told someone what Swatch Time it was: @" + html[0] + ".")
        return        

    elif '!move' in message.content.lower():       
        discordMessage = message.content       
        partUno = discordMessage.split(sep=' <#')
        if len(partUno) != 2:
            await message.channel.send("You wanna try that again bud?")
            return
        else:
            findChannel = partUno[1].split(sep='>')            
            realChannel = client.get_channel(int(findChannel[0]))    
            if message.reference == None:
                await message.channel.send("You have to reply to a message.")
                return
            else:
                msg = message.reference.message_id                    
                msgText = await message.channel.fetch_message(msg)                               
                await msgText.delete()
                if len(msgText.content) > 0:
                    await realChannel.send(msgText.content)
                if len(msgText.attachments) > 0:
                    for x in range(len(msgText.attachments)):
                        await realChannel.send(msgText.attachments[x].url)
                print(message.author.name + " moved " + msgText.author.name + "\'s message to #" + str(realChannel) + ".")
                return

    # Uwu'ifies messages            
    elif '!uwu' in message.content.lower():
        discordMessage = message.content.split(sep=' ')
        if len(discordMessage) == 1:
            if message.reference == None: # No reply or message
                await message.channel.send("You didn't write or reply to anything, dingus.")
                return

            else:
                msg = message.reference.message_id
                msgText = await message.channel.fetch_message(msg)
                msgText = msgText.content.lower()
                await message.channel.send(uwu.uwuReply(msgText))
                return
                
        elif len(discordMessage) > 1: # If wrote a message
            msgText = message.content.split (" ", 1)
            await message.channel.send(uwu.uwuText(msgText))
            return

    elif '!deez' in message.content.lower():
        deezNuts = random.sample(words.words(), 1)
        await message.channel.send(deezNuts[0] + deezList[random.randint(0,(len(deezList))-1)])
        return
                      
    elif 'http' in message.content.lower(): # Checks if message contains a link.
        # Exempts links directly to skeb artist pages
        if 'skeb' in message.content.lower():
            if 'works' not in message.content.lower():
                return
        elif 'meltyblood.club' in message.content.lower():
            return
               
        # Splits the link(s) into individual string(s).        
        discordMessage = message.content.lower()
        if reposti.reposti(discordMessage, message.guild.name):
            await message.channel.send(f'<@{message.author.id}> <:Reposti:781288738843656222> '+ # Ladies and gentlemen, we got 'em.
                    'General Reposti! You are an old one.')
            currentTime = ['DATE', 'HOUR', 'MINUTE', 'SECOND']                    
            tempList = str(message.created_at).split(sep=' ')
            currentTime[0] = tempList[0]
            timeList = tempList[1].split(sep=':')
            if int(timeList[0]) <= 4:
                realHours = int(timeList[0]) + 8
            else:
                realHours = int(timeList[0]) - 4 

            currentTime[1] = str(realHours)
            currentTime[2] = timeList[1]
            finalList = timeList[2].split(sep='.')
            currentTime[3] = finalList[0]
            print(message.author.name + f" reposti'd in Hammertown at " +
                currentTime[1] + ':' + currentTime[2] + ':' + currentTime[3] + ', on ' + currentTime[0] + '.'
            )
            return        

client.run(TOKEN)
