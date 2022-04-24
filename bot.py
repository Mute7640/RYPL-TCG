#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Konstantin (k0nze) Lübeck"
__copyright__   = "Copyright 2021, Discord Bot Template"
__credits__     = ["Alex Ronquillo: https://realpython.com/how-to-make-a-discord-bot-python/"]

__license__     = "BSD 3-Clause License"
__version__     = "0.1"
__contact__     = {
                    "Twitch": "https://twitch.tv/k0nze",
                    "Youtube": "https://youtube.com/k0nze",
                    "Twitter": "https://twitter.com/k0nze_gg",
                    "Instagram": "https://instagram.com/k0nze.gg",
                    "Discord": "https://discord.k0nze.gg",
                }

import os
import json
import discord
import random

from os.path import join, dirname
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import commands

# load .env file
dir_path = os.path.dirname(os.path.realpath(__file__))

dotenv_path = join(dir_path, '.env')
load_dotenv(dotenv_path)

DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

JSON_FILE = str(os.path.dirname(os.path.realpath(__file__))) + '/data.json'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    """ Runs once the bot has established a connection with Discord """

    print(f'{bot.user.name} has connected to Discord')

    # check if bot has connected to guilds
    if len(bot.guilds) > 0:
        print('connected to the following guilds:')

        for guild in bot.guilds:
            print(f'* {guild.name}#{guild.id}')


@bot.command(name="claim")
async def on_claim(ctx):
    """
    Runs when the !claim command was issued in a Discord text channel and posts a 
    random GIF from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content

    # log event on command line
    print(f'* "{author.name}" issued "{command}" in "{channel}" of "{guild}"')

    # post random GIF from the JSON file
    await channel.send(get_random_claim_link())

@bot.command(name="view")
async def on_view(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content

    await channel.send("The current players are: Kareem/\Mute/\SIXlows ICON/\SIXlows/\SUVPQN/\Kensai/\Monki/\Wazabi/\Doancoan/\ZylexiusDev/\Ebenezsaro/\Kensai National Treasure")

def get_random_claim_link():
    """ Returns a random gif link from the JSON file """
    with open(JSON_FILE) as json_file:
        # open JSON file
        data = json.load(json_file)
        # get all gifs
        claims = data['claims']
        # randomly select a gif
        claim = random.choice(claims)

        # return the link of the gif to the caller
        return claim['link']
        
@bot.command(name="viewkareem")
async def on_viewkareem(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("https://i.imgur.com/TRyLU6R.png")

    
@bot.command(name="viewdoancoan")
async def on_viewdoancoan(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("https://i.imgur.com/CcZw78V.png")

@bot.command(name="viewwazabi")
async def on_viewwazabi(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("https://i.imgur.com/a65yQwY.png")

@bot.command(name="viewmonki")
async def on_viewmonki(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("https://i.imgur.com/HcpcuuW.png")

@bot.command(name="viewkensai")
async def on_viewkensai(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("https://i.imgur.com/dm3K06z.png")

@bot.command(name="viewsuvqpn")
async def on_viewsuvqpn(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("https://i.imgur.com/IdUMjkF.png")

@bot.command(name="view6lows")
async def on_view6lows(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("https://i.imgur.com/JqMGyRl.png")

@bot.command(name="view6lowsicon")
async def on_view6lowsicon(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("https://i.imgur.com/QdZLTTP.png")

@bot.command(name="viewmute")
async def on_viewmute(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("https://i.imgur.com/1PlLsUi.png")

@bot.command(name="viewebenezerasaro")
async def on_viewebenezerasaro(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("https://i.imgur.com/aZMskdV.png")

@bot.command(name="viewzylexiusdev")
async def on_viewezylexiusdev(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("https://i.imgur.com/gdjrzwj.png")



@bot.command(name="helpme")
async def on_helppls(ctx):
    """
    Runs when the !view command was issued in a Discord text channel and posts a 
    players from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content
    await channel.send("```Yo you want help aight time to go supersonic do view then the players name no space for example !viewmute you can do !helpview for the full list```")



if __name__ == "__main__":
    # launch bot
    bot.run(DISCORD_TOKEN)
