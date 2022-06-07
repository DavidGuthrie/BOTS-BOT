# import discord
# import asyncio
# import os
# import json
# import random
# import requests
# from urllib import request
# from discord.utils import get
# from discord.ext import commands, tasks
# from discord.ext.commands import has_permissions, CheckFailure

# # API links 

# jokeurl = "https://dad-jokes.p.rapidapi.com/random/joke" #joke api 3
# #url = "http://icanhazdadjoke.com/" #joke api 2
# #url = "http://official-joke-api.appspot.com/random_joke" #joke api
# rand = "https://uselessfacts.jsph.pl/random.json?language=en" #random facts api

# client = discord.Client()
# client = commands.Bot(command_prefix = '+')
# client.remove_command('help')

# # Bot logon

# @client.event
# async def on_ready():
#   print('{0.user} is here, nothing to fear!'.format(client))

#   @client.event
#   async def on_message(message):

#     # Embeds

#     if message.content.startswith('+help'):

#       embed=discord.Embed(title=f"Help Commands", description="List of help commands, all start with a + example: +joke", color=0xFFFF00)
#       embed.set_author(name="Encrypto", icon_url="")
#       # embed.add_field(name="welcome", value="Welcome help text", inline=True) Need to develop welcome text
#       embed.add_field(name="joke", value="Joke repository", inline=True)
#       embed.add_field(name="mnstrsprice", value="Blockmonsters current price via CoinGecko", inline=True)
#       embed.add_field(name="chart", value="Blockmonsters chart", inline=True)
#       # embed.add_field(name="docs", value="Documentation for the project", inline=True)
#       # embed.add_field(name="tasks", value="Daily tasks to perform", inline=True)
#       # embed.add_field(name="level", value="Provides link to community level", inline=True)
#       # embed.add_field(name="contract", value="contract details for Island Group DAO", inline=True)
#       # embed.add_field(name="treasury", value="Treasury wallet address", inline=True)
#       embed.add_field(name="random", value="Random facts", inline=True)
#       embed.add_field(name="8ball & Question", value="Ask a question to the 8ball, 8ball Will $palm reach $50", inline=True)
#       embed.add_field(name="rps", value="Let's have a game of Rock, Paper or Scissors", inline=True)
      
#       embed.set_thumbnail(url="")
#       embed.set_footer(text="$mnstrs4Lyfe   |   http://blockmonsters.co ")
#       await message.channel.send(embed=embed)

#     if message.content.startswith('+mnstrsprice'):
#       palm_info = get_coingecko_info()

#       embed=discord.Embed(title= palm_info['name'], description="Some useful info about $mnstrs (source: CoinGecko)", color=0xFFFF00)
#       embed.set_author(name="Encrypto", icon_url="")
#       #Current Price
#       embed.add_field(name="Current Fiat Price", value= 
#       "${:,.7f}".format(palm_info['cur_price_usd']) + "\n" + 
#       "€{:,.7f}".format(palm_info['cur_price_eur']) + "\n" + 
#       "£{:,.7f}".format(palm_info['cur_price_gbp']) + "\n" + 
#       "₩{:,.7f}".format(palm_info['cur_price_krw']), inline=True)

#       # embed.add_field(name="Current Price", value= 
#       # "{:,.7f} BTC".format(palm_info['cur_price_btc']) + "\n" + 
#       # "{:,.7f} ETH".format(palm_info['cur_price_eth']) + "\n" + 
#       # "{:,.7f} BNB".format(palm_info['cur_price_bnb']), inline=True)

#       #Price change
#       embed.add_field(name="Price Change ($)", value= 
#       "24h: " + "{:.3%}".format(palm_info['price_24h']/100) + "\n" + 
#       "7d:  " + "{:.3%}".format(palm_info['price_7d']/100) + "\n" + 
#       "14d: " + "{:.3%}".format(palm_info['price_14d']/100) + "\n" + 
#       "30d: " + "{:.3%}".format(palm_info['price_30d']/100), inline=True)
    
#       #Market cap / volume
#       #embed.add_field(name="Current Marketcap", value= "${:,.2f}".format(palm_info['market_cap']), inline=True)
#       #embed.add_field(name="24h Trading Volume", value= "${:,.2f}".format(palm_info['volume_24h']), inline=True)
#       #embed.add_field(name="CoinGecko Rank", value= "#" + str(palm_info['cg_rank']), inline=True)

#       embed.set_thumbnail(url="")
#       embed.set_footer(text="$mnstrs4Lyfe")
#       await message.channel.send(embed=embed)

#     await client.process_commands(message)

#     msg = message.content

#     if message.author == client.user:
#       return

#     print(msg)

#     # Moderation  

#     for i in range(0,len(message.author.roles)):
#       if message.author.roles[i].name == 'COOLDOWN':
#         if msg.lower().startswith('cooldown'):
#           if len(message.mentions) != 0 and len(message.mentions) < 2:
#             await message.channel.send('Uh oh! Someone has been bad! 😪')
#             await cooldown(message.mentions[0], message)

#   # Report Spam in separate channel - replace channel to #ReportSpam

#     if msg.lower().startswith('giveaway'): 
#       server_id = message.guild.id
#       channel_id = message.channel.id
#       msg_id = message.id
#       link = 'https://discordapp.com/channels/' + str(server_id) + '/' + str(channel_id) + '/' + str(msg_id)
#       channel = client.get_channel(983473726739857448)
#       await channel.send(f"{message.author.mention} Report Spam {link}") 
   
#     #Error catch example 
#     if msg.lower().startswith('error'):
#       try:
#         1/0
#       except Exception:
#         await message.channel.send("I can't do that")

#     # bot response commands 
#     bot_responses = {
#       # Text based listener
#       'ffs' : "🙄 ...drama queen",
#       'shut up' : "NO U",
#       'hello botsbot' : "Hello, my friend! 🙂",
#       'what can you do botsbot' : "That is none of your concern",
#       # Emoji based listener
#       '💩' : "Pooooooooop",
#       '👋' : "Are you waving to me? 🤩",
#       # Commands
#       '+level' : "<https://atlasbot.xyz/leaderboard/>",
#       '+docs' : "<https://uploads-ssl.webflow.com/61b7ef3f6e1160ab79341eda/61bfb0e71d0781ced4233c31_Blockpaper.pdf>",
#       '+roadmap' : "https://discord.com/channels/877924849849364540/879500773808037907/982045783358586891",     
#       '+chart' : "TBA",
 
#     }

#     if msg.lower() in bot_responses:
#       await message.channel.send(bot_responses[msg.lower()])

#     # Welcomes
#     # Reaction Based Emojis
          
#     # Custom Animated Emoji Based Listeners

#     # elif msg.startswith('<a:palm>'):
#     #   await message.channel.send('Text')  

#     # Custom Static Emoji Based Listeners
      
#     elif msg.startswith('<a:mnstrloading>'): #change emoji
#       await message.channel.send('mnstrs to $1!')
#       await asyncio.sleep(1)
#       await message.channel.send('NFA 😂')
      
#     # Text Based Listeners

#     # elif msg.lower().startswith('ahah'):
#     #   await message.channel.send('<:Ahah:874404430634704896>')

#     elif msg.lower().startswith('+joke'):
#       await retrieveJoke(message)

#     elif msg.lower().startswith('+random'):
#       await retrieveRand(message)

#     elif msg.lower().startswith('mnstrs is hot'):
#       await message.channel.send('I am a BOT.....')
#       await asyncio.sleep(1)
#       await message.channel.send('......')
#       await asyncio.sleep(1)
#       await message.channel.send('......')
#       await asyncio.sleep(1)
#       await message.channel.send('......on 🔥')

#   # Ban User, updated ban text in separate channel 
#   # channel = ADD CHANNEL 

#   @client.command(aliases=['Ban','BAN'])
#   @commands.has_permissions(ban_members=True)
#   async def ban(ctx, member : discord.Member, *, reason=None):
#     channel = client.get_channel(983473726739857448)
#     await member.ban(reason=reason)
#     await channel.send(f"{member.mention} has been banned.")

#   # Game commands

#   @client.command(aliases=['8ball'], pass_context=True)
#   async def _8ball(ctx, *, question):
#     responses = ['It is certain.',
#                'It is decidedly so.',
#                'Without a doubt.',
#                'Yes - definitely',
#                'You may rely on it',
#                'As I see it, yes.',
#                'Most likely',
#                'Outlook good.',
#                'Yes.',
#                'Signs point to yes.',
#                'Reply hazy, try again.',
#                'Ask again later.',
#                'Better not tell you now.',
#                'Cannot predict now',
#                'Concentrate and ask again.',
#                "Don't count on it.",
#                'My reply is no.',
#                'My sources say no.',
#                'Outlook not so good.',
#                'Very doubtful.']
#     await ctx.send(f'Question: {question}\n **8ball shakes**\n 8ball: {random.choice(responses)}')

# # Rock Paper Scissors
# @client.command(aliases = ['rps'])
# async def _rps(ctx):
#   await ctx.send(f"{ctx.author.mention} Let's play a game! Pick Rock, Paper, or Scissors!")
#   bots_pick = random.choice(["Rock","Paper","Scissors"]).lower()
#   #await ctx.send("I picked " + bots_pick)
#   try:
#     answer = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout = 10)

#     try:
#       ans = answer.content.lower()

#       if (ans == "rock"):
#         if (bots_pick == "rock"):
#           await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - Tie!")
#         elif (bots_pick == "paper"):
#           await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You lost!")
#         else:
#           await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You won!")
#       elif (ans == "paper"):
#         if (bots_pick == "rock"):
#           await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You won!")
#         elif (bots_pick == "paper"):
#           await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - Tie!")
#         else:
#           await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You lost!")
#       elif (ans == "scissors"):
#         if (bots_pick == "rock"):
#           await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You lost!")
#         elif (bots_pick == "paper"):
#           await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - You won!")
#         else:
#           await ctx.send(f"{ctx.author.mention} I picked " + bots_pick + ", you picked " + ans + " - Tie!")
#       else:
#         await ctx.send(f"{ctx.author.mention} Pick a valid answer. Restart to try again")
#     #await ctx.send("You picked " + ans)
#     except ValueError:
#       await ctx.send("Invalid response")

#   except asyncio.TimeoutError:
#     await ctx.send(f"{ctx.author.mention} You waited too long, game over!")
#     await asyncio.sleep(0.1)
#     await ctx.send(f"{ctx.author.mention} Thank you for wasting my time, deducting 1000 mnsyts from your balance! :imp: ")

# # Cooldown Function

# async def cooldown(member, message):
#   role = discord.utils.get(member.guild.roles, name="COOLDOWN")
#   await member.add_roles(role)
#   await message.channel.send('<@' + str(member.id) + '> needs to cooldown for a bit in <#983473726739857448!')
  
#   await timing()

#   await member.remove_roles(role)
#   await message.channel.send('<@' + str(member.id) + '> Has cooled down. They can chat freely again!')
#   return

# # Timer Function

# async def timing():
#   for i in range(0,60): # Seconds you wish to cooldown
#     await asyncio.sleep(1)
#     i = i + 1

# # Retrieve Joke Function

# #old call 
# # async def retrieveJoke(message):
# #   r = request.urlopen(url)
# #   data = r.read()
# #   jsonData = json.loads(data)
# #   await message.channel.send(jsonData.get(str('joke')))
#   # await message.channel.send(jsonData.get(str('setup')) + '...')
#   # await asyncio.sleep(2)
#   # await message.channel.send(jsonData.get(str('punchline')))

# async def retrieveJoke(message):
#   headers = {
#     'x-rapidapi-key': "ac33982a50msh2a843ee53cb4fabp19a303jsn78bba0d5b4f1",
#     'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
#     }
#   joke_json = requests.get(jokeurl, headers=headers).json()
#   await message.channel.send(joke_json['body'][0]['setup'] + '...')
#   await asyncio.sleep(2)
#   #await message.channel.send(joke_json['body'][0]['punchline'])
#   punch = await message.channel.send(joke_json['body'][0]['punchline'])
#   await punch.add_reaction("🤣")
#   if joke_json['body'][0]['NSFW'] == True:
#     await punch.add_reaction("🔞")

# # Random facts retrieval

# async def retrieveRand(message):
#   r = request.urlopen(rand)
#   data = r.read()
#   jsonData = json.loads(data)
#   await message.channel.send(jsonData.get(str('text')))

# # CoingGecko price detail retrieval

# def get_coingecko_info():
#     gc_url = "https://api.coingecko.com/api/v3/coins/block-monsters"
#     response = requests.get(gc_url)
#     blockmonsters_inf = {
#     'name'         : response.json()['name'],
#     'cur_price_usd': response.json()['market_data']['current_price']['usd'],
#     'cur_price_eur': response.json()['market_data']['current_price']['eur'],
#     'cur_price_gbp': response.json()['market_data']['current_price']['gbp'],
#     'cur_price_krw': response.json()['market_data']['current_price']['krw'],
#     'cur_price_btc': response.json()['market_data']['current_price']['btc'],
#     'cur_price_eth': response.json()['market_data']['current_price']['eth'],
#     'cur_price_bnb': response.json()['market_data']['current_price']['bnb'],
#     'price_24h'    : response.json()['market_data']['price_change_percentage_24h'],
#     'price_7d'     : response.json()['market_data']['price_change_percentage_7d'],
#     'price_14d'    : response.json()['market_data']['price_change_percentage_14d'],
#     'price_30d'    : response.json()['market_data']['price_change_percentage_30d'],
#     'market_cap'   : response.json()['market_data']['market_cap']['usd'],
#     'volume_24h'   : response.json()['market_data']['total_volume']['usd'],
#     'cg_rank'      : response.json()['market_data']['market_cap_rank'],
#     'bscsan'       : response.json()['platforms']['binance-smart-chain'],
#     }
#     return blockmonsters_inf

# token = os.environ.get("TOKEN")
# client.run(token)