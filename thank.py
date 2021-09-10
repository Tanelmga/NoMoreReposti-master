import os
import discord

def thank(discordMessage):

    splitList = discordMessage.split(sep=' ')
    if '!thank' in splitList[0] and len(splitList) >= 2:
        if 'reposti' in discordMessage:
            return True
        elif 'bot' in discordMessage:
            return True
        else:
            return False            
    else:
        return True
