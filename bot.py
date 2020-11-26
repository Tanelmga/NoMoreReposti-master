# NoMoreReposti

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    
    print(f'{client.user} has connected to Discord!') # Let's me know this fucker is working.

async def on_guild_join(guild): # Creates a text file to manage links on server join.
    
    f = open(f'{guild.name} linkList.txt', 'x')
    f.close()
    f = open(f'{guild.name} linkList.txt', 'w')
    f.write("My hovercraft is full of eels.\n")
    f.close()
    print("Link list for server \"" + guild.name + "\" created successfully.")

@client.event
async def on_message(message):
    
    if message.author == client.user: # Bot ignores its own messages.
        return    
   
    if '!reposti' in message.content.lower(): # Ignore messages with "!reposti".
        return

    elif 'http' in message.content.lower(): # Checks if message contains a link.
               
        # Splits the link(s) into individual string(s).
        links = []
        splitList = message.content.split(sep=' ')
        for x in range(len(splitList)):
            if 'http' in splitList[x]:                
                links.append(splitList[x])
        for x in range(len(links)): # Culls unneeded URL info
            if 'twitter' in links[x]: 
                questionKill = links[x].split(sep='?')
                links[x] = questionKill[0]

        # Converts all links in existing file to a list.
        f = open(f'{message.guild.name} linkList.txt', 'r')
        linkList = f.readlines()
        f.close()        
        while len(linkList) >= 100: # Culls old links when there are more than 1000.
            del linkList[0]
            f = open(f'{message.guild.name} linkList.txt', 'w')
            f.write(linkList)
            f.close()

        for y in range(len(links)): # Loops through the links that were just posted and checks them against all old links.
            for x in linkList:
                if x == links[y] + '\n':
                    await message.channel.send(
                        f'<@{message.author.id}> <:Reposti:781288738843656222> '+ # Ladies and gentlemen, we got him.
                        'General Reposti! You are an old one.'
                        )
                    # Command line logging.
                    # Don't look at this. It's hideous and only here so I can be nosy. 
                    currentTime = ['DATE', 'HOUR', 'MINUTE', 'SECOND']                    
                    tempList = str(message.created_at).split(sep=' ')
                    currentTime[0] = tempList[0]
                    timeList = tempList[1].split(sep=':')
                    realHours = int(timeList[0]) - 5 
                    currentTime[1] = str(realHours)
                    currentTime[2] = timeList[1]
                    finalList = timeList[2].split(sep='.')
                    currentTime[3] = finalList[0]
                    print(message.author.name + f" reposti'd in {message.guild.name} at " +
                        currentTime[1] + ':' + currentTime[2] + ':' + currentTime[3] + ', on ' + currentTime[0] + '.'
                    )
                    break            
        f = open(f'{message.guild.name} linkList.txt', 'a') # Appends newly posted links to the text file. 
        for y in range(len(links)):
            f.write(links[y] + '\n')
        f.close()
        return        

client.run(TOKEN)
