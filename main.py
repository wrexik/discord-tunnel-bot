from ast import alias
from ipaddress import ip_address
import discord
from pyautogui import sleep
from pyngrok import ngrok
from discord.ext import commands
import os
import aiohttp
import requests
import random


#Made with Love - Wrexik
#please run ngrok authtoken *your token* before setting up tunnels

bot_name = "Sitara"                               #change to your's bot name
default_activity = "Tvoji Mamu 🤭"               #sets activity after connecting to dc
twitch_username = "notwrexik"                    #your twitch username (lowercase only pls :D) ofc you can let it be like that 😉
bot_secret = "" #paste your bot secret
port = "25565"                                   #your minecraft server port
bot_pfp = "https://i.postimg.cc/63vzgSPN/round-sitara.png" #your's bot profile picture


twitch_link = "https://www.twitch.tv/" + twitch_username    #don't edit this
intents = discord.Intents.all()                             #don't edit this
client = discord.Client(intents=discord.Intents.default())  #don't edit this
bot = commands.Bot(command_prefix="!",intents=intents)      #don't edit this
tunnels = ngrok.get_tunnels()                               #don't edit this

@bot.event
async def on_ready():
    #connect to dc
    print(f'{bot.user} Je tady ❤️❤️❤️')
    await bot.change_presence(activity=discord.Streaming(name='Tvoji Mamu 🤭', url= twitch_link))

@client.event
async def on_error():
    print(f'{bot.user} Had an error')

#End of setup part

@bot.command(aliases=["stat"]) #sends status of tunnel
async def status(ctx):
    #sends status of tunnel
    print(f'{ctx.author} requested server status')
    await ctx.send(f"{ctx.author.mention} Getting Status... 😊")
    tunnels = ngrok.get_tunnels()
    if tunnels == []:
        online = False
    else:
        online = True
    
    if online == True:
        embed=discord.Embed(title= bot_name, description="Online", color=0x00ff2a)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/large-green-circle_1f7e2.png")
        embed.set_footer(text="Wrexik")
        embed.set_author(name= bot_name, icon_url= bot_pfp)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title= bot_name, description="Offline", color=0xff0000)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/large-red-circle_1f534.png")
        embed.set_footer(text="Wrexik")
        embed.set_author(name= bot_name, icon_url= bot_pfp)
        await ctx.send(embed=embed)


@bot.command(aliases=['adresa', 'pripojit'])
async def ip(ctx):
    print(f'{ctx.author} Requested IP')
    await ctx.send(f'{ctx.author.mention} Requested IP 😊')

    tunnels = ngrok.get_tunnels()
    if tunnels == []:
        embed=discord.Embed(title= bot_name, description="Server Offline", color=0xff0000)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/cross-mark_274c.png")
        embed.add_field(name="Try !start", value="none", inline=False)
        embed.set_footer(text="Wrexik")
        embed.set_author(name=  bot_name, icon_url= bot_pfp)
        await ctx.send(embed=embed)
        online = True
    else:
        embed=discord.Embed(title="Server Online", color=0x00ff2a)
        embed.set_author(name= bot_name)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/check-mark-button_2705.png")
        embed.add_field(name="IP:", value=tunnels, inline=False)
        embed.set_footer(text="Wrexik")
        embed.set_author(name=  bot_name, icon_url= bot_pfp)
        await ctx.send(embed=embed)
        online = False

@bot.command(aliases=['stop', 'shutdown'])
async def close(ctx):
    print(f'{ctx.author} Stopped ngrok tcp connection')
    embed=discord.Embed(title= bot_name, description="Stopped Server Connection", color=0xff0000)
    embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/stop-sign_1f6d1.png")
    embed.add_field(name="Try !start", value="none", inline=False)
    embed.set_footer(text="Wrexik")
    embed.set_author(name=  bot_name, icon_url= bot_pfp)
    await ctx.send(embed=embed)
    ngrok.kill()

@bot.command(aliases=['open']) #starts ngrok (25565) tunnel
async def start(ctx):
    #starts ngrok (25565) tunnel
    print(f'{ctx.author} Started ngrok tcp connection ✅')
    ngrok.connect(port, "tcp")
    tunnels = ngrok.get_tunnels()
    embed=discord.Embed(title= bot_name, description="Connection Started", color=0x00ff2a)
    embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/check-mark-button_2705.png")
    embed.add_field(name="IP:", value=tunnels, inline=False)
    embed.set_footer(text="Wrexik")
    embed.set_author(name=  bot_name, icon_url= bot_pfp)
    await ctx.send(embed=embed)
    sleep(0.5)
    await ctx.send("Make sure to reset the connection after 2 hours! 🙏")

@bot.command(aliases=['reboot'])
async def restart(ctx):
    tunnels = ngrok.get_tunnels()
    if tunnels == []:
        print(f'{ctx.author} Requested restart but no tunnel is running')
        await ctx.send(f'{ctx.author.mention} No tunnel is running at the monment')
        embed=discord.Embed(title= bot_name, description="Tunnel not running", color=0xff0000)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/cross-mark_274c.png")
        embed.add_field(name="Try !start", value="none", inline=False)
        embed.set_footer(text="Wrexik")
        embed.set_author(name=  bot_name, icon_url= bot_pfp)
        await ctx.send(embed=embed)
    else:
        print(f'{ctx.author} Is restarting ngrok tcp connection')
        await ctx.send(f'{ctx.author} Is restarting ngrok tcp connection')
        sleep(3)
        print(f'{ctx.author} Restarting Now! 🔃')
        embed=discord.Embed(title= bot_name, description="Restarting Now!", color=0x00fbff)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/clockwise-vertical-arrows_1f503.png")
        embed.add_field(name="IP:", value="none", inline=True)
        embed.set_footer(text="Wrexik")
        embed.set_author(name=  bot_name, icon_url= bot_pfp)
        await ctx.send(embed=embed)
        ngrok.kill()
        sleep(3)
        ngrok.connect(port, "tcp")
        tunnels = ngrok.get_tunnels()
        embed=discord.Embed(title="Connection Restarted!", color=0x1eff00)
        embed.set_author(name= bot_name)
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/check-mark-button_2705.png")
        embed.add_field(name="IP:", value=tunnels, inline=False)
        embed.set_footer(text="Wrexik")
        embed.set_author(name=  bot_name, icon_url= bot_pfp)
        await ctx.send(embed=embed)

#End of ngrok part

@client.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed(title=f"Error!!!", description=f"Command not found. Try **!h**")
        await ctx.send(f'{ctx.author.mention}'" Command not found. Try **!h**")


@bot.command(aliases=["creator", "wrexik"])
async def git(ctx):
    await ctx.send(f'{ctx.author.mention}'" this is my creator https://github.com/wrexik")





@bot.command(aliases=["h"])
async def pomoct(ctx):
    embed = discord.Embed(title='Help - !h', color = 0xbb00ff)
    embed.add_field(name="!status - Get's status of the server", value= '1')
    embed.add_field(name="!ip - Send's IP of the tunnel (server)", value= '2')
    embed.add_field(name="!close - Close's the tunnel", value= '3')
    embed.add_field(name="!start - Start's tcp connection localhost:port -> ngrok", value= '4')
    embed.add_field(name="!restart - Restart's connection to ngrok and send's new ip address", value= '5')
    embed.add_field(name="!wrexik - shows info about creator", value= '6')
    embed.add_field(name="!motd (Message) Edit's bots status", value= '7')
    embed.add_field(name="!say (Message) - Repeat's message like a parrot 🦜", value= '8')
    embed.add_field(name="!pes / !boba - Send's random picture of dog", value= '10')
    embed.add_field(name="!meme - Post's random Meme", value= '11')
    embed.add_field(name="!cat - Send's random picture of cat", value= '12')
    embed.add_field(name="!dice - Rolls the dice", value= '13')
    embed.set_author(name= bot_name, icon_url= bot_pfp)
    await ctx.send(embed=embed)
    print(f'{ctx.author} Requested help')

@bot.command()
async def motd(ctx, *args):
    print(f'{ctx.author} requested motd')

    message=""
    for arg in args:
        message = message + " " + arg

    await bot.change_presence(activity= discord.Streaming(name= message, url= twitch_link))
    await ctx.send(f'{ctx.author.mention}'" changed status of the bot to "f'**{message}**!')

@bot.command(aliases=['say', 'opakuj'])
async def rekni(ctx, *args):
    print(f'{ctx.author} requested rekni')
    response = ""
    
    for arg in args:
        response = response + " " + arg
    await ctx.channel.send(response)

    await bot.change_presence(activity= discord.Streaming(name= message, url= twitch_link))
    await ctx.send(f'{ctx.author.mention}'" changed status of the bot to "f'**{message}**!')


@bot.command(aliases=['boba', 'guta', "peso"])
async def pes(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()
      embed = discord.Embed(title="Boba a Guta™️", color=discord.Color.purple()) # Create embed
      embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
      embed.set_author(name=  bot_name, icon_url= bot_pfp)
      await ctx.send(embed=embed) # Send the embed
      print(f'{ctx.author} Requested dog pics')

@bot.command()
async def meme(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/meme')
      memejson = await request.json()
      embed = discord.Embed(title="Boba a Guta™️", color=discord.Color.purple()) # Create embed
      embed.set_image(url=memejson['image']) # Set the embed image to the value of the 'link' key
      embed.set_author(name=  bot_name, icon_url= bot_pfp)
      await ctx.send(embed=embed) # Send the embed
      print(f'{ctx.author} Requested meme')

@bot.command(aliases=['kocka', 'hermelin'])
async def cat(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/cat')
      catjson = await request.json()
      embed = discord.Embed(title="Boba a Guta™️", color=discord.Color.purple()) # Create embed
      embed.set_image(url=catjson['link']) # Set the embed image to the value of the 'link' key
      embed.set_author(name=  bot_name, icon_url= bot_pfp)
      await ctx.send(embed=embed) # Send the embed
      print(f'{ctx.author} Requested cat pics')

@bot.command(aliases=['kostka', 'roll'])
async def dice(ctx):
    async with aiohttp.ClientSession() as session:  
        rolled = random.randint(1, 6)

        if rolled == 1:
            await ctx.send('Tvoje kouzelné číslo je 1️⃣') # Send the rolled number
        if rolled == 2:
            await ctx.send('Tvoje kouzelné číslo je 2️⃣') # Send the rolled number
        if rolled == 3:
            await ctx.send('Tvoje kouzelné číslo je 3️⃣') # Send the rolled number
        if rolled == 4:
            await ctx.send('Tvoje kouzelné číslo je 4️⃣') # Send the rolled number
        if rolled == 5:
            await ctx.send('Tvoje kouzelné číslo je 5️⃣') # Send the rolled number
        if rolled == 6:
            await ctx.send('Tvoje kouzelné číslo je 6️⃣') # Send the rolled number
        
    print(f'{ctx.author} Requested dice roll: ' f'{rolled}') # Log




bot.run(bot_secret)
