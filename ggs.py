import os
import random
import discord

ggMsg = ['ggs',
         'ggs',
         'ggs',
         'gs',
         'bgs but ok',
         'didn\'t ask',
         'ggs dude!!']

def ggs():
    return ggMsg[random.randint(0, len(ggMsg)-1)]
