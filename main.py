import discord
import asyncio
import os
import json
import random
import requests
from urllib import request
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure

# API links 

jokeurl = "https://dad-jokes.p.rapidapi.com/random/joke" #joke api 3
#url = "http://icanhazdadjoke.com/" #joke api 2
#url = "http://official-joke-api.appspot.com/random_joke" #joke api
rand = "https://uselessfacts.jsph.pl/random.json?language=en" #random facts api

client = discord.Client()
client = commands.Bot(command_prefix = '+')
client.remove_command('help')

# Bot logon

@client.event
async def on_ready():
  print('{0.user} is here, nothing to fear!'.format(client))

  @client.event
  async def on_message(message):

    # Embeds

    if message.content.startswith('+help'):

      embed=discord.Embed(title=f"Help Commands", description="List of help commands, all start with a + example: +joke", color=0xFFFF00)
      embed.set_author(name="Encrypto", icon_url="https://s2.coinmarketcap.com/static/img/coins/64x64/11777.png")
      # embed.add_field(name="welcome", value="Welcome help text", inline=True) Need to develop welcome text
      embed.add_field(name="joke", value="Joke repository", inline=True)
      embed.add_field(name="mnstrsprice", value="Blockmonsters current price via CoinGecko", inline=True)
      embed.add_field(name="chart", value="Blockmonsters chart", inline=True)
      # embed.add_field(name="docs", value="Documentation for the project", inline=True)
      # embed.add_field(name="tasks", value="Daily tasks to perform", inline=True)
      # embed.add_field(name="level", value="Provides link to community level", inline=True)
      # embed.add_field(name="contract", value="contract details for Island Group DAO", inline=True)
      # embed.add_field(name="treasury", value="Treasury wallet address", inline=True)
      embed.add_field(name="random", value="Random facts", inline=True)
      embed.add_field(name="8ball & Question", value="Ask a question to the 8ball, 8ball Will $mnstrs reach $50", inline=True)
      embed.add_field(name="rps", value="Let's have a game of Rock, Paper or Scissors", inline=True)
      embed.add_field(name="effects", value="Provides a breakdown of all the currently available buffs and debuffs you can receive from an attack", inline=True)
      embed.add_field(name="{blockmon name}", value="Provides Attack moves, types, amount of attacks & ailment/enhancement received/given", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)

    if message.content.startswith('+effects'):
      embed=discord.Embed(title=f"Ailments/Enhancements", description="Descriptions of the Attack Status Effects", color=0xFF0000)
      embed.set_author(name="Encrypto", icon_url="https://s2.coinmarketcap.com/static/img/coins/64x64/11777.png")
      embed.add_field(name="Ailments", value= 
      "**Scared**" + " - " + "Accuracy, Attack & Defense decrease\n\u200b"
      "**Diseased**" + " - " + "3% hp drain each round & reduced Defense and       Accuracy, minor attack and speed boost\n\u200b"
      "**Drowning**" + " - " + "1% hp drain each round & Speed, Accuracy & Attack decrease\n\u200b" 
      "**Confused**" + " - " + "Accuracy and Attack decrease\n\u200b"
      "**Cursed**" + " - " + "Attack, Speed, Defese & Accuracy slight decrease\n\u200b"
      "**Hacked**" + " - " + "Unable to attack for two turns\n\u200b"
      "**Burning**" + " - " + "4% hp drain each round & Defense, Speed and Accuracy slighty decreased, slight Attack increase\n\u200b"
      "**Poisoned**" + " - " + "5% hp drain each round & Defense and Speed slighty decrease\n\u200b", inline=True)
      embed.add_field(name="Enhancements", value=
      "**Stealth**" + " - " + "Defense, Speed & Accuracy increase\n\u200b"
      "**Sleepy**" + " - " + "Miss one round, but gain 25% hp back\n\u200b"
      "**Energized**" + " - " + "Temporary boost to all stats\n\u200b" 
      "**Sniper**" + " - " + "Power & Attack increase with Defense decrease(+Critical hit) next attack\n\u200b"
      "**Boost**" + " - " + "Speed, Attack, Defense & Accuracy increase\n\u200b"
      "**Sprint**" + " - " + "Speed increase - Accuracy, Defense & Attack slight decrease\n\u200b"
      "**Guarded**" + " - " + "Blocks next attack\n\u200b"
      "**Hyped**" + " - " + "-10% hp & a boost to all stats\n\u200b"
      "**GuardianAngel**" + " - " + "Revives blockmon upon 0hp and slight Attack & Speed increase\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)
    
    if message.content.startswith('+flamisire'):

      embed=discord.Embed(title=f"Flamisire", description="Attacks & Status Ailments/Enhancements", color=0xDE6038)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Tackle" + "\n\n\u200b" + "Quick Hands" + "\n\n\u200b" + "Fire Spit", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" + "\n\n\u200b" + "Normal/25" + "\n\n\u200b" + "Fire/5", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Scared" + "\n\n\u200b" + "Sprint" + "\n\n\u200b" + "Burning", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b814191e41c2166ca31_1-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)

    if message.content.startswith('+flamince'):

      embed=discord.Embed(title=f"Flamince", description="Attacks & Status Ailments/Enhancements", color=0xDE6038)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Pound" + "\n\n\u200b" + "Quick Hands" +  "\n\n\u200b" + "Blaze Jump" +  "\n\n\u200b" + "Fire Blow", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Normal/25" +  "\n\n\u200b" + "Fire/5" +  "\n\n\u200b" + "Fire/5", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Boost" +  "\n\n\u200b" + "Sprint" +  "\n\n\u200b" + "Burning" +  "\n\n\u200b" + "Burning", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b813a6b5332f4a89d21_13232-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)

    if message.content.startswith('+blazing'):

      embed=discord.Embed(title=f"Blazing", description="Attacks & Status Ailments/Enhancements", color=0xDE6038)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Blaze Jump" + "\n\n\u200b" + "Psychic Ball" +  "\n\n\u200b" + "Inferno" +  "\n\n\u200b" + "Cut", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Fire/25" +  "\n\n\u200b" + "Psychic/25" +  "\n\n\u200b" + "Fire/25" +  "\n\n\u200b" + "Normal/25", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Burning" +  "\n\n\u200b" + "Scared" +  "\n\n\u200b" + "Burning" +  "\n\n\u200b" + "Diseased", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b81fe492d50ae92b5d3_13233-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)  

    if message.content.startswith('+orcalf'):

      embed=discord.Embed(title=f"Orcalf", description="Attacks & Status Ailments/Enhancements", color=0x5E95D3)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Whirlpool" + "\n\n\u200b" + "Tackle" +  "\n\n\u200b" + "Water Ball" +  "\n\n\u200b", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Water/25" +  "\n\n\u200b" + "Normal/25" +  "\n\n\u200b" + "Water/5" +  "\n\n\u200b", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Sprint" +  "\n\n\u200b" + "Scared" +  "\n\n\u200b" + "Drowning" +  "\n\n\u200b", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b800e256b79aeec7010_13234-min-p-500.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)  

    if message.content.startswith('+orcaphin'):

      embed=discord.Embed(title=f"Orcaphin", description="Attacks & Status Ailments/Enhancements", color=0x5E95D3)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Water Ball" + "\n\n\u200b" + "Tackle" +  "\n\n\u200b" + "Water Wave"  +  "\n\n\u200b" + "Pound", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Water/5" +  "\n\n\u200b" + "Normal/25" +  "\n\n\u200b" + "Water/5"  +  "\n\n\u200b" + "Normal/25", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Sprint" +  "\n\n\u200b" + "Scared" +  "\n\n\u200b" + "Drowning"  +  "\n\n\u200b" + "Boost", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b81bbaa8f9b89695635_13235-min-p-500.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)  

    if message.content.startswith('+whirsel'):

      embed=discord.Embed(title=f"Whirsel", description="Attacks & Status Ailments/Enhancements", color=0x5E95D3)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Whirlpool" + "\n\n\u200b" + "Night Beam" +  "\n\n\u200b" + "Hydro Blast"  +  "\n\n\u200b" + "Shadow Sneak", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Water/25" +  "\n\n\u200b" + "Ghost/5" +  "\n\n\u200b" + "Water/3"  +  "\n\n\u200b" + "Ghost/5", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Sprint" +  "\n\n\u200b" + "Scared" +  "\n\n\u200b" + "Drowning"  +  "\n\n\u200b" + "Boost", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b813a6b53aecea89d20_13236-min-p-500.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)  

    if message.content.startswith('+petaliz'):

      embed=discord.Embed(title=f"Petaliz", description="Attacks & Status Ailments/Enhancements", color=0x419656)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Grass Knot" + "\n\n\u200b" + "Tackle" +  "\n\n\u200b" + "Pound" +  "\n\n\u200b", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Grass/25" +  "\n\n\u200b" + "Normal/25" +  "\n\n\u200b" + "Normal/25" +  "\n\n\u200b", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Sleepy" +  "\n\n\u200b" + "Scared" +  "\n\n\u200b" + "Boost" +  "\n\n\u200b", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b81e91e74baba111049_13237-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)  

    if message.content.startswith('+lizatoon'):

      embed=discord.Embed(title=f"Lizatoon", description="Attacks & Status Ailments/Enhancements", color=0x419656)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Grass Knot" + "\n\n\u200b" + "Grass Vine" +  "\n\n\u200b" + "Tackle"  +  "\n\n\u200b" + "Razor Leaf", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Grass/25" +  "\n\n\u200b" + "Grass/5" +  "\n\n\u200b" + "Normal/3"  +  "\n\n\u200b" + "Grass/5", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Sleepy" +  "\n\n\u200b" + "Sleepy" +  "\n\n\u200b" + "Scared"  +  "\n\n\u200b" + "Diseased", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b800b5f3db5772fbae6_13238-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+lizarex'):

      embed=discord.Embed(title=f"Lizarex", description="Attacks & Status Ailments/Enhancements", color=0x419656)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Quick Hands" + "\n\n\u200b" + "Dragon Breath" +  "\n\n\u200b" + "Green Candle"  +  "\n\n\u200b" + "Grass Vine", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Dragon/3" +  "\n\n\u200b" + "Grass/3"  +  "\n\n\u200b" + "Grass/5", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Sprint" +  "\n\n\u200b" + "Burning" +  "\n\n\u200b" + "Poisoned"  +  "\n\n\u200b" + "Sleepy", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b81889584d769f303d1_13239-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)  

    if message.content.startswith('+blakan'):

      embed=discord.Embed(title=f"Blakan", description="Attacks & Status Ailments/Enhancements", color=0x634B3F)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Tackle" + "\n\n\u200b" + "Rock Bash" +  "\n\n\u200b" + "Rock Punch"  +  "\n\n\u200b" + "Pound", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Rock/5" +  "\n\n\u200b" + "Rock/5"  +  "\n\n\u200b" + "Normal/25", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Scared" +  "\n\n\u200b" + "Sprint" +  "\n\n\u200b" + "Harden"  +  "\n\n\u200b" + "Boost", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b81b966a34f6c68b79a_13243-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)  

    if message.content.startswith('+mikado'):

      embed=discord.Embed(title=f"Mikado", description="Attacks & Status Ailments/Enhancements", color=0xBD803F)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Cut" + "\n\n\u200b" + "Choke" +  "\n\n\u200b" + "Upper Cut"  +  "\n\n\u200b" + "Quick Hands", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Fighting/5" +  "\n\n\u200b" + "Fighting/5"  +  "\n\n\u200b" + "Normal/25", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Diseased" +  "\n\n\u200b" + "Harden" +  "\n\n\u200b" + "Energised"  +  "\n\n\u200b" + "Sprint", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b8190761b27e2a6dff3_13245-min-p-500.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)  

    if message.content.startswith('+baybee'):

      embed=discord.Embed(title=f"Baybee", description="Attacks & Status Ailments/Enhancements", color=0xD2B740)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Tackle" + "\n\n\u200b" + "Pulse Shock" +  "\n\n\u200b" + "Pound"  +  "\n\n\u200b" + "Electric Jump", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Electric/25" +  "\n\n\u200b" + "Normal/25"  +  "\n\n\u200b" + "Electric/5", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Scared" +  "\n\n\u200b" + "Energised" +  "\n\n\u200b" + "Boost"  +  "\n\n\u200b" + "Stealth", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd3b81f35b7e1e06d20b33_13246-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+kyoot'):

      embed=discord.Embed(title=f"Kyoot", description="Attacks & Status Ailments/Enhancements", color=0x419656)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Tackle" + "\n\n\u200b" + "Quick Hands" +  "\n\n\u200b" + "Grass Knot"  +  "\n\n\u200b" + "Razor Leaf", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Normal/25" +  "\n\n\u200b" + "Grass/25"  +  "\n\n\u200b" + "Grass/5", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Scared" +  "\n\n\u200b" + "Sprint" +  "\n\n\u200b" + "Sleepy"  +  "\n\n\u200b" + "Diseased", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd4152cb2b3d0e3e0f4ae7_13249-min-p-500.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+verani'):

      embed=discord.Embed(title=f"Verani", description="Attacks & Status Ailments/Enhancements", color=0x7A7A7A)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Pound" + "\n\n\u200b" + "Grass Knot" +  "\n\n\u200b" + "Tornado Bash"  +  "\n\n\u200b" + "Mind Play", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Grass/25" +  "\n\n\u200b" + "Flying/25"  +  "\n\n\u200b" + "Psychic/25", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Boost" +  "\n\n\u200b" + "Sleepy" +  "\n\n\u200b" + "Guarded"  +  "\n\n\u200b" + "Cursed", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd41522b4cb62c6a47bfb7_13253-min-p-500.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+elareon'):

      embed=discord.Embed(title=f"Elareon", description="Attacks & Status Ailments/Enhancements", color=0xB263C6)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Pound" + "\n\n\u200b" + "Mind Play" +  "\n\n\u200b" + "Psychic Ball"  +  "\n\n\u200b" + "Tele Kick", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Psychic/25" +  "\n\n\u200b" + "Psychic/5"  +  "\n\n\u200b" + "Psychic/3", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Boost" +  "\n\n\u200b" + "Cursed" +  "\n\n\u200b" + "Scared"  +  "\n\n\u200b" + "Stealth", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd415273f587e3667574cd_13254-min-p-500.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+baliga'):

      embed=discord.Embed(title=f"Baliga", description="Attacks & Status Ailments/Enhancements", color=0x419656)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Pound" + "\n\n\u200b" + "Green Candle" +  "\n\n\u200b" + "Grass Knot"  +  "\n\n\u200b" + "Grass Vine", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Grass/3" +  "\n\n\u200b" + "Grass/25"  +  "\n\n\u200b" + "Grass/5", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Boost" +  "\n\n\u200b" + "Poisoned" +  "\n\n\u200b" + "Sleepy"  +  "\n\n\u200b" + "Sleepy", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd415273f587612e7574dd_13255-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+maying'):

      embed=discord.Embed(title=f"Maying", description="Attacks & Status Ailments/Enhancements", color=0x6BB7B4)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Pound" + "\n\n\u200b" + "Slashing Wing" +  "\n\n\u200b" + "Wingslash"  +  "\n\n\u200b" + "Sky Drill", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Flying/5" +  "\n\n\u200b" + "Flying/3"  +  "\n\n\u200b" + "Flying/3", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Boost" +  "\n\n\u200b" + "Sprint" +  "\n\n\u200b" + "Diseased"  +  "\n\n\u200b" + "GuardianAngel", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd41528820626dd7c533d1_13256-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+bussaeus'):

      embed=discord.Embed(title=f"Bussaeus", description="Attacks & Status Ailments/Enhancements", color=0x419656)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Pound" + "\n\n\u200b" + "Green Vine" +  "\n\n\u200b" + "Razor Leaf"  +  "\n\n\u200b" + "Giga Blast", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Grass/5" +  "\n\n\u200b" + "Grass/5"  +  "\n\n\u200b" + "Normal/3", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Boost" +  "\n\n\u200b" + "Sleepy" +  "\n\n\u200b" + "Diseased"  +  "\n\n\u200b" + "Boost", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd415260b8ae6674a64790_13257-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+gronea'):

      embed=discord.Embed(title=f"Gronea", description="Attacks & Status Ailments/Enhancements", color=0xDE6038)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Pound" + "\n\n\u200b" + "Blaze Jump" +  "\n\n\u200b" + "Fire Blow" +  "\n\n\u200b" + "Giga Blast", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Fire/5" +  "\n\n\u200b" + "Fire/5" +  "\n\n\u200b" + "Normal/3", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Boost" +  "\n\n\u200b" + "Burning" +  "\n\n\u200b" + "Burning" +  "\n\n\u200b" + "Boost", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd4152d2eb9d3c1ebc8079_13258-min-p-800.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed)

    if message.content.startswith('+benjia'):

      embed=discord.Embed(title=f"Benjia", description="Attacks & Status Ailments/Enhancements", color=0xD2B740)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Lightning Ball" + "\n\n\u200b" + "Night Beam" +  "\n\n\u200b" + "Peekaboo"  +  "\n\n\u200b" + "Pound", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Electric/5" +  "\n\n\u200b" + "Ghost/5" +  "\n\n\u200b" + "Ghost/25"  +  "\n\n\u200b" + "Normal/25", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Energised" +  "\n\n\u200b" + "Cursed" +  "\n\n\u200b" + "Confused"  +  "\n\n\u200b" + "Boost", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd415249969046ef20b5d0_13259-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+linkme'):

      embed=discord.Embed(title=f"Linkme", description="Attacks & Status Ailments/Enhancements", color=0xD899E5)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Tackle" + "\n\n\u200b" + "Mind Play" +  "\n\n\u200b" + "Pound"  +  "\n\n\u200b" + "Cryptic Claw", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Psychic/25" +  "\n\n\u200b" + "Normal/25"  +  "\n\n\u200b" + "Cryptic/25", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Scared" +  "\n\n\u200b" + "Cursed" +  "\n\n\u200b" + "Boost"  +  "\n\n\u200b" + "Congested", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd41534cd575ea1a32bbfb_13260-min-p-500.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+shillox'):

      embed=discord.Embed(title=f"Shillox", description="Attacks & Status Ailments/Enhancements", color=0x7A7A7A)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Giga Blast" + "\n\n\u200b" + "Mind Play" +  "\n\n\u200b" + "Upper Cut"  +  "\n\n\u200b" + "Cryptic Claw", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/3" +  "\n\n\u200b" + "Psychic/25" +  "\n\n\u200b" + "Fight/5"  +  "\n\n\u200b" + "Cryptic/25", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Boost" +  "\n\n\u200b" + "Cursed" +  "\n\n\u200b" + "Energised"  +  "\n\n\u200b" + "Congested", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd41532b4cb6759c47bfb8_13265-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+keti'):

      embed=discord.Embed(title=f"Keti", description="Attacks & Status Ailments/Enhancements", color=0x6BB7B4)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Tornado Bash" + "\n\n\u200b" + "Pound" +  "\n\n\u200b" + "Tackle"  +  "\n\n\u200b" + "Slashing Wing", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Flying/25" +  "\n\n\u200b" + "Normal/25" +  "\n\n\u200b" + "Normal/25"  +  "\n\n\u200b" + "Flying/5", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Guarded" +  "\n\n\u200b" + "Boost" +  "\n\n\u200b" + "Scared"  +  "\n\n\u200b" + "Sprint", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd44533c8bf82b1a8a1b02_13267-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+riotter'):

      embed=discord.Embed(title=f"Riotter", description="Attacks & Status Ailments/Enhancements", color=0x634B3F)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Tackle" + "\n\n\u200b" + "Rock Bash" +  "\n\n\u200b" + "Pound"  +  "\n\n\u200b" + "Rock Punch", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Rock/5" +  "\n\n\u200b" + "Normal/25"  +  "\n\n\u200b" + "Rock/5", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Scared" +  "\n\n\u200b" + "Sprint" +  "\n\n\u200b" + "Boost"  +  "\n\n\u200b" + "Harden", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd4453fe492d022d92e55e_13274-min-p-500.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+rioles'):

      embed=discord.Embed(title=f"Rioles", description="Attacks & Status Ailments/Enhancements", color=0x634B3F)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Pound" + "\n\n\u200b" + "Rock Bash" +  "\n\n\u200b" + "Boulder Toss"  +  "\n\n\u200b" + "Dragon Tongue", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Rock/5" +  "\n\n\u200b" + "Rock/3"  +  "\n\n\u200b" + "Dragon/5", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Boost" +  "\n\n\u200b" + "Sprint" +  "\n\n\u200b" + "Boost"  +  "\n\n\u200b" + "Hyped", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd445490761bcee9a70da8_13275-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+arlionce'):

      embed=discord.Embed(title=f"Arlionce", description="Attacks & Status Ailments/Enhancements", color=0x634B3F)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Dragon Breath" + "\n\n\u200b" + "Cut" +  "\n\n\u200b" + "Dragon Bash"  +  "\n\n\u200b" + "Rock n Roll", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Dragon/3" +  "\n\n\u200b" + "Normal/25" +  "\n\n\u200b" + "Dragon/3"  +  "\n\n\u200b" + "Rock/3", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Burning" +  "\n\n\u200b" + "Diseased" +  "\n\n\u200b" + "Burning"  +  "\n\n\u200b" + "Guarded", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd4454f35b7e03fdd24f1b_13276-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

      if message.content.startswith('+stonk'):

       embed=discord.Embed(title=f"Stonk", description="Attacks & Status Ailments/Enhancements", color=0x7A7A7A)
       embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
       embed.add_field(name="Attacks" + "\n\n\u200b", value= "Cut" + "\n\n\u200b" + "Tackle" +  "\n\n\u200b" + "Pound"  +  "\n\n\u200b" + "Drop Kick", inline=True)
       embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Normal/25" +  "\n\n\u200b" + "Normal/25" +  "\n\n\u200b" + "Normal/25"  +  "\n\n\u200b" + "Fight/5", inline=True)
       embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Guarded" +  "\n\n\u200b" + "Diseased" +  "\n\n\u200b" + "Scared"  +  "\n\n\u200b" + "Hyped", inline=True)
       embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
       embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd44549824572b6c712aa6_13282-min-p-500.png")
       embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
       await message.channel.send(embed=embed) 

    if message.content.startswith('+jaguh'):

      embed=discord.Embed(title=f"Jaguh", description="Attacks & Status Ailments/Enhancements", color=0x419656)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Razor Leaf" + "\n\n\u200b" + "Cut" +  "\n\n\u200b" + "Lightning Ball"  +  "\n\n\u200b" + "Grass Vine", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Grass/25" +  "\n\n\u200b" + "Normal/25" +  "\n\n\u200b" + "Electric/5"  +  "\n\n\u200b" + "Grass/3", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Diseased" +  "\n\n\u200b" + "Diseased" +  "\n\n\u200b" + "Energised"  +  "\n\n\u200b" + "Sleepy", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd4454499690cef620c63f_13284-min.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 

    if message.content.startswith('+saphiosys'):

      embed=discord.Embed(title=f"Saphiosys", description="Attacks & Status Ailments/Enhancements", color=0xD899E5)
      embed.set_author(name="Encrypto", icon_url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61b7f915817606d7c9e11639_image0%20(1)%202.png")
      embed.add_field(name="Attacks" + "\n\n\u200b", value= "Virus Punch" + "\n\n\u200b" + "Hackathon" +  "\n\n\u200b" + "Cryptic Claw"  +  "\n\n\u200b" + "Mechanic Laser", inline=True)
      embed.add_field(name="Type/Amount" + "\n\n\u200b", value= "Psychic/5" +  "\n\n\u200b" + "Psychic/3" +  "\n\n\u200b" + "Cryptic/25"  +  "\n\n\u200b" + "Psychic/3", inline=True)
      embed.add_field(name="Ailment/Enhancement" + "\n\n\u200b", value= "Congested" +  "\n\n\u200b" + "Hacked" +  "\n\n\u200b" + "Congested"  +  "\n\n\u200b" + "Sniper", inline=True)
      embed.add_field(name="\n\n\u200b", value= "\n\n\u200b", inline=True)
      embed.set_thumbnail(url="https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bd4467f75288235a066851_13285-min-p-800.png")
      embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
      await message.channel.send(embed=embed) 
    
    if message.content.startswith('+mnstrsprice'):
      mnstrs_info = get_coingecko_info()

      embed=discord.Embed(title= mnstrs_info['name'], description="Some useful info about $mnstrs (source: CoinGecko)", color=0xFFFF00)
      embed.set_author(name="Encrypto", icon_url="")
      #Current Price
      embed.add_field(name="Current Fiat Price", value= 
      "${:,.7f}".format(mnstrs_info['cur_price_usd']) + "\n" + 
      "€{:,.7f}".format(mnstrs_info['cur_price_eur']) + "\n" + 
      "£{:,.7f}".format(mnstrs_info['cur_price_gbp']) + "\n" + 
      "R${:,.7f}".format(mnstrs_info['cur_price_brl']), inline=True)

      embed.add_field(name="Current Price", value= 
      # "{:,.7f} BTC".format(mnstrs_info['cur_price_btc']) + "\n" + 
      "{:,.7f} ETH".format(mnstrs_info['cur_price_eth']) + "\n" + 
      "{:,.7f} BNB".format(mnstrs_info['cur_price_bnb']), inline=True)

      #Price change
      embed.add_field(name="Price Change ($)", value= 
      "24h: " + "{:.3%}".format(mnstrs_info['price_24h']/100) + "\n" + 
      "7d:  " + "{:.3%}".format(mnstrs_info['price_7d']/100) + "\n" + 
      "14d: " + "{:.3%}".format(mnstrs_info['price_14d']/100) + "\n" + 
      "30d: " + "{:.3%}".format(mnstrs_info['price_30d']/100), inline=True)
    
      #Market cap / volume
      #embed.add_field(name="Current Marketcap", value= "${:,.2f}".format(palm_info['market_cap']), inline=True)
      #embed.add_field(name="24h Trading Volume", value= "${:,.2f}".format(palm_info['volume_24h']), inline=True)
      #embed.add_field(name="CoinGecko Rank", value= "#" + str(palm_info['cg_rank']), inline=True)

      embed.set_thumbnail(url="")
      embed.set_footer(text="$mnstrs4Lyfe")
      await message.channel.send(embed=embed)

    await client.process_commands(message)

    msg = message.content

    if message.author == client.user:
      return

    print(msg)

    # Moderation  

    for i in range(0,len(message.author.roles)):
      if message.author.roles[i].name == 'COOLDOWN':
        if msg.lower().startswith('cooldown'):
          if len(message.mentions) != 0 and len(message.mentions) < 2:
            await message.channel.send('Uh oh! Someone has been bad! 😪')
            await cooldown(message.mentions[0], message)

  # Report Spam in separate channel - replace channel to #ReportSpam

    if msg.lower().startswith('giveaway'): 
      server_id = message.guild.id
      channel_id = message.channel.id
      msg_id = message.id
      link = 'https://discordapp.com/channels/' + str(server_id) + '/' + str(channel_id) + '/' + str(msg_id)
      channel = client.get_channel(983473726739857448)
      await channel.send(f"{message.author.mention} Report Spam {link}") 
   
    #Error catch example 
    if msg.lower().startswith('error'):
      try:
        1/0
      except Exception:
        await message.channel.send("I can't do that")

    # bot response commands 
    bot_responses = {
      # Text based listener
      'ffs' : "🙄 ...drama queen",
      'shut up' : "NO U",
      'hello botsbot' : "Hello, my friend! 🙂",
      'what can you do botsbot' : "That is none of your concern",
      # Emoji based listener
      '💩' : "Pooooooooop",
      '👋' : "Are you waving to me? 🤩",
      # Commands
      '+level' : "<https://atlasbot.xyz/leaderboard/983418279588663396>",
      '+docs' : "<https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bfb0e71d0781ced4233c31_Blockpaper.pdf>",
      '+roadmap' : "<https://discord.com/channels/877924849849364540/879500773808037907/982045783358586891>",     
      '+chart' : "<https://charts.bogged.finance/?c=bsc&t=0x287Db351d5230716246CfB46AF8153025eDa6A0a>"
      
 
    }

    if msg.lower() in bot_responses:
      await message.channel.send(bot_responses[msg.lower()])

    # Welcomes
    # Reaction Based Emojis
      
    elif msg.startswith('hang'): 
      await message.add_reaction('😈')
      
    elif msg.startswith('drey'): 
      await message.add_reaction('<a:commanderrank:988837728273694730>')
       
    # Custom Animated Emoji Based Listeners

    # elif msg.startswith('<a:palm>'):
    #   await message.channel.send('Text')  

    # Custom Static Emoji Based Listeners
      
    elif msg.startswith('<a:mnstrloading:936206170392260619>'): #change emoji
      await message.channel.send('mnstrs to $1!')
      await asyncio.sleep(1)
      await message.channel.send('NFA 😂')
      
    # Text Based Listeners

    # elif msg.lower().startswith('ahah'):
    #   await message.channel.send('<:Ahah:874404430634704896>')

    elif msg.lower().startswith('+joke'):
      await retrieveJoke(message)

    elif msg.lower().startswith('+random'):
      await retrieveRand(message)

    elif msg.lower().startswith('bot is hot'):
      await message.channel.send('I am a BOT.....')
      await asyncio.sleep(1)
      await message.channel.send('......')
      await asyncio.sleep(1)
      await message.channel.send('......')
      await asyncio.sleep(1)
      await message.channel.send('......on 🔥')

  # Ban User, updated ban text in separate channel 
  # channel = ADD CHANNEL 

  @client.command(aliases=['Ban','BAN'])
  @commands.has_permissions(ban_members=True)
  async def ban(ctx, member : discord.Member, *, reason=None):
    channel = client.get_channel(983473726739857448)
    await member.ban(reason=reason)
    await channel.send(f"{member.mention} has been banned.")

  # Game commands

  @client.command(aliases=['8ball'], pass_context=True)
  async def _8ball(ctx, *, question):
    responses = ['It is certain.',
               'It is decidedly so.',
               'Without a doubt.',
               'Yes - definitely',
               'You may rely on it',
               'As I see it, yes.',
               'Most likely',
               'Outlook good.',
               'Yes.',
               'Signs point to yes.',
               'Reply hazy, try again.',
               'Ask again later.',
               'Better not tell you now.',
               'Cannot predict now',
               'Concentrate and ask again.',
               "Don't count on it.",
               'My reply is no.',
               'My sources say no.',
               'Outlook not so good.',
               'Very doubtful.']
    await ctx.send(f'Question: {question}\n **8ball shakes**\n 8ball: {random.choice(responses)}')

# Rock Paper Scissors
@client.command(aliases = ['rps'])
async def _rps(ctx):
  await ctx.send(f"{ctx.author.mention} Let's play a game! Pick Rock, Paper, or Scissors!")
  bots_pick = random.choice(["Rock","Paper","Scissors"]).lower()
  #await ctx.send("I picked " + bots_pick)
  try:
    answer = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout = 10)

    try:
      ans = answer.content.lower()

      if (ans == "rock"):
        if (bots_pick == "rock"):
          await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - Tie!")
        elif (bots_pick == "paper"):
          await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You lost!")
        else:
          await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You won!")
      elif (ans == "paper"):
        if (bots_pick == "rock"):
          await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You won!")
        elif (bots_pick == "paper"):
          await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - Tie!")
        else:
          await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You lost!")
      elif (ans == "scissors"):
        if (bots_pick == "rock"):
          await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You lost!")
        elif (bots_pick == "paper"):
          await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You won!")
        else:
          await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - Tie!")
      else:
        await ctx.send(f"{ctx.author.mention} Pick a valid answer. Restart to try again")
    #await ctx.send("You picked " + ans)
    except ValueError:
      await ctx.send("Invalid response")

  except asyncio.TimeoutError:
    await ctx.send(f"{ctx.author.mention} You waited too long, game over!")
    await asyncio.sleep(0.1)
    await ctx.send(f"{ctx.author.mention} Thank you for wasting my time, deducting 1000 mnstrs from your balance! :imp: ")

   # Cooldown Function

async def cooldown(member, message):
  role = discord.utils.get(member.guild.roles, name="COOLDOWN")
  await member.add_roles(role)
  await message.channel.send('<@' + str(member.id) + '> needs to cooldown for a bit in <#983449774571290684!')
  
  await timing()

  await member.remove_roles(role)
  await message.channel.send('<@' + str(member.id) + '> Has cooled down. They can chat freely again!')
  return

# Timer Function

async def timing():
  for i in range(0,60): # Seconds you wish to cooldown
    await asyncio.sleep(1)
    i = i + 1

# Retrieve Joke Function

#old call 
# async def retrieveJoke(message):
#   r = request.urlopen(url)
#   data = r.read()
#   jsonData = json.loads(data)
#   await message.channel.send(jsonData.get(str('joke')))
  # await message.channel.send(jsonData.get(str('setup')) + '...')
  # await asyncio.sleep(2)
  # await message.channel.send(jsonData.get(str('punchline')))

async def retrieveJoke(message):
  headers = {
    'x-rapidapi-key': "ac33982a50msh2a843ee53cb4fabp19a303jsn78bba0d5b4f1",
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }
  joke_json = requests.get(jokeurl, headers=headers).json()
  await message.channel.send(joke_json['body'][0]['setup'] + '...')
  await asyncio.sleep(2)
  #await message.channel.send(joke_json['body'][0]['punchline'])
  punch = await message.channel.send(joke_json['body'][0]['punchline'])
  await punch.add_reaction("🤣")
  if joke_json['body'][0]['NSFW'] == True:
    await punch.add_reaction("🔞")

# Random facts retrieval

async def retrieveRand(message):
  r = request.urlopen(rand)
  data = r.read()
  jsonData = json.loads(data)
  await message.channel.send(jsonData.get(str('text')))

# CoingGecko price detail retrieval

def get_coingecko_info():
    gc_url = "https://api.coingecko.com/api/v3/coins/block-monsters"
    response = requests.get(gc_url)
    blockmonsters_inf = {
    'name'         : response.json()['name'],
    'cur_price_usd': response.json()['market_data']['current_price']['usd'],
    'cur_price_eur': response.json()['market_data']['current_price']['eur'],
    'cur_price_gbp': response.json()['market_data']['current_price']['gbp'],
    'cur_price_brl': response.json()['market_data']['current_price']['brl'],
    'cur_price_btc': response.json()['market_data']['current_price']['btc'],
    'cur_price_eth': response.json()['market_data']['current_price']['eth'],
    'cur_price_bnb': response.json()['market_data']['current_price']['bnb'],
    'price_24h'    : response.json()['market_data']['price_change_percentage_24h'],
    'price_7d'     : response.json()['market_data']['price_change_percentage_7d'],
    'price_14d'    : response.json()['market_data']['price_change_percentage_14d'],
    'price_30d'    : response.json()['market_data']['price_change_percentage_30d'],
    'market_cap'   : response.json()['market_data']['market_cap']['usd'],
    'volume_24h'   : response.json()['market_data']['total_volume']['usd'],
    'cg_rank'      : response.json()['market_data']['market_cap_rank'],
    'bscsan'       : response.json()['platforms']['binance-smart-chain'],
    }
    return blockmonsters_inf

token = os.environ.get("TOKEN")
client.run(token)