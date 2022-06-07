# Code that can create a ticker on the side of the Disc server, , so code redundant atm, need to import 'from yahoo_fin import stock_info as si'
import discord
import yahoo_fin
from discord.ext import commands
from yahoo_fin import stock_info as si

client = discord.Client()

def read_token():
  with open('botTokenPath.txt', 'r') as f:
    lines = f.readlines()
    return lines[0].strip()

@client.command()
async def run(ctx):
  while True:
    change = si.get_quote_data("MNSTRS")

    name="MNSTRS: \n$"+ str(round(si.get_live_price("MNSTRS"),2))+ "("+str(round(change["regularMarketChangePercent"],2))+")"+"%"
    await ctx.guild.me.edit(nick=name)