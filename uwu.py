# uwu.py

import os
import discord

def uwuReply(msgText):  
    
        msgUwu1 = msgText.replace("l", 'w')
        msgUwu2 = msgUwu1.replace('r', 'w')
        msgUwu3 = msgUwu2.replace('this', 'dis')
        msgUwu4 = msgUwu3.replace('thewe', 'dewe')
        msgUwu5 = msgUwu4.replace('that', 'dat')
        if len(msgUwu5) < 1997:
            return (msgUwu5 + ' uwu')                    
        else:
            return msgUwu5

def uwuText(msgText):

    msgText[1] = msgText[1].lower()
    msgUwu1 = msgText[1].replace("l", 'w')
    msgUwu2 = msgUwu1.replace('r', 'w')
    msgUwu3 = msgUwu2.replace('this', 'dis')
    msgUwu4 = msgUwu3.replace('there', 'dewe')
    msgUwu5 = msgUwu4.replace('that', 'dat')
    if len(msgUwu5) < 1997:
        return (msgUwu5 + ' uwu')            
    else:
        return msgUwu5
            
