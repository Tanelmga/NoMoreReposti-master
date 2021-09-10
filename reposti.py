import os
import discord

def reposti(discordMessage, discordName):

    links = []
    splitList = discordMessage.split(sep=' ')
    for x in range(len(splitList)):
        if 'http' in splitList[x]:                
            links.append(splitList[x])
    for x in range(len(links)): # Culls unneeded URL info in Twitter links
        if 'twitter' in links[x]: 
            flagKill = links[x].split(sep='?')
            links[x] = flagKill[0]
    for x in range(len(links)): 
        if 'youtube' in links[x]: 
            y = links[x].split(sep='=')
            for z in range (len(y)):
                if '&' in y[z]:
                    flagKill = y[z].split(sep='&')
                    links[x] = flagKill[0]
                    break
                else:
                    links[x] = y[z]                                        
    for x in range(len(links)): # These isolate the Youtube video code from the URL
        if 'youtu.be' in links[x]: 
            y = links[x].split(sep='/')
            flagKill = y[3].split(sep='?')
            links[x] = flagKill[0]
        

    # Converts all links in existing file to a list.
    f = open(f'{discordName} linkList.txt', 'r')
    linkList = f.readlines()
    f.close()        
    while len(linkList) >= 250: # Culls old links when there are more than 250.
        del linkList[0]
        f = open(f'{discordName} linkList.txt', 'w')
        f.write(linkList[0])
        f.close()
        del linkList[0]
        for x in range(len(linkList)):
            f = open(f'{discordName} linkList.txt', 'a')
            f.write(linkList[x])
            f.close()            

    for y in range(len(links)): # Loops through the links that were just posted and checks them against all old links.
        for x in linkList:
            if x == links[y] + '\n':          
                return True               
                                      
    f = open(f'Hammertown linkList.txt', 'a') # Appends newly posted links to the text file. 
    for y in range(len(links)):
        f.write(links[y] + '\n')
    f.close()
