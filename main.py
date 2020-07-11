import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import os
import sys
import asyncio
import random
from random import randint
import inspect
import requests
from dotenv import load_dotenv
import json
import aiohttp
import time

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=">")
bot.remove_command("help")

@bot.command()
async def ping(ctx): 
  await ctx.send(str("Pong"))

@bot.command()
async def match(ctx, *, member: discord.Member):
  match = random.choice(ctx.guild.members)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "A good match for `{0.display_name}` would be `@{1.name}#{1.discriminator} ({1.display_name})!`".format(member, match))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)
  
@bot.command()
async def howgay(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% gay!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howstupid(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% stupid!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howvirgin(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% virgin!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howmidget(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% midget!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howbottom(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% bottom!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howtop(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% top!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howswitch(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% switch!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howtall(ctx, *, member: discord.Member):
  feet = str(randint(1,6))
  inch = str(randint(1,11))
  rand = feet + "'" + inch
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)
  
@bot.command()
async def howfamilyfriendly(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% familyfriendly!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howsimp(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% a simp!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)
  
@bot.command()
async def howfemboy(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% femboy!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)
  
@bot.command()
async def howcis(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% cis!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howbi(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% bisexual!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howasexual(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% asexual!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)
  
@bot.command()
async def howpan(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% pan!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def ppsize(ctx, *, member: discord.Member):
  rand = randint(0,20)
  pp = "=" * rand
  string = "8" + pp + "D"
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}'s pp".format(member), value = "`{1}`".format(member, string))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def coochiesize(ctx, *, member: discord.Member):
  rand = randint(0,20)
  pp = "-" * rand
  string = "(" + pp + ")"
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}'s coochie".format(member), value = "`{1}`".format(member, string))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)
  
@bot.command()
async def howfurry(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% fur!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howgray(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% graysexual!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)
  
@bot.command()
async def howtrans(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% trans!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howhorny(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% horny!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)
  
@bot.command()
async def howlesbian(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% lesbian!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howstraight(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% straight!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
async def howcute(ctx, *, member: discord.Member):
  rand = randint(1,100)
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member), value = "`{0.display_name}` is {1}% cute!".format(member, rand))
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1, 40, commands.BucketType.user)
async def whoiscuter(ctx, member1: discord.Member, member2: discord.Member):
  rand1 = randint(1,100)
  rand2 = 100 - rand1
  em = discord.Embed(title = "", description = "", color = 0x7d386f)
  em.add_field(name = "{0.name}".format(member1), value = "`{0.display_name}` **is** __*{1}%*__ **cute**".format(member1, rand1))
  em.add_field(name = "{0.name}".format(member2), value = "`{0.display_name}` **is** __*{1}%*__ **cute**".format(member2, rand2))
  em.add_field(name = "LGBOT", value = "A bot driven by the gays © LGBOT")

  if rand1 > rand2 :
   em.add_field(name = "Result", value = "`{0.display_name}` **is cuter than** `{1.display_name}`".format(member1, member2))

  if rand1 < rand2 :
   em.add_field(name = "Result", value = "`{0.display_name}` **is cuter than** `{1.display_name}`".format(member2, member1))

  if rand1 == 50 :
    em.add_field(name = "Result", value = "`{0.display_name}` **is equally as cute as** `{1.display_name}`".format(member1, member2))

                 
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)
  
@whoiscuter.error
async def whoiscuter_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = "You're on cooldown! You have {:.2f} seconds left".format(error.retry_after)
    await ctx.send(msg)
  else:
    raise error

@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def gif(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=CZJC57epC7rOUXNXP57vncK1GtrPvdZL')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=CZJC57epC7rOUXNXP57vncK1GtrPvdZL&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
        embed.set_footer(text = "Bot by Trainsgender") 

    await session.close()

    await ctx.send(embed=embed)

@gif.error
async def gif_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = "You're on cooldown! You have {:.2f} seconds left".format(error.retry_after)
    await ctx.send(msg)
  else:
    raise error

@bot.command()
async def coinflip(ctx):
  temp = ["Heads", "Tails"]
  var1 = random.choice(temp)
  await ctx.send(var1)

@bot.command()
async def diceroll(ctx, value):
  try:
    value = int(value)
  except ValueError:
    pass

  rand = randint(1, value)
  await ctx.send("........  :game_die: : " + "***" + str(rand) + "***")

@diceroll.error
async def diceroll_error(ctx, error):
  if isinstance(error, commands.CommandInvokeError):
    msg = "That's not a valid number of sides"
    await ctx.send(msg)
  else:
    raise error
  
@bot.command()

async def randomizers(ctx):
  em = discord.Embed(title = "LGBOT", description = "Randomizer commands", color = 0x7d386f)
  em.add_field(name = "`>howgay <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howbi <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howasexual <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howpan <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howfurry <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howgray <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howfemboy <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howcis <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howhorny <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howtrans <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howlesbian <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howstraight <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howcute <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howsimp <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howbottom <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howmidget <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howtop <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howvirgin <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howstupid <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howswitch <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>howtall <mention>`", value = "Measures you")
  em.add_field(name = "`>howfamilyfriendly <mention>`", value = "Gives a percentage")
  em.add_field(name = "`>match <mention>`", value = "Finds you a good match to date")
  em.add_field(name = "`>ppsize <mention>`", value = "How big is pp")
  em.add_field(name = "`>coochiesize <mention>`", value = "How big is coochie")
  em.add_field(name = "`>coinflip`", value = "Heads or tails")
  em.add_field(name = "`>diceroll <number of sides>`", value = ":game_die:")
  em.add_field(name = "`>whoiscuter <mention> <mention>`", value = ":pleading_face:")
  
  
  em.set_footer(text = "Bot by Trainsgender") 
  await ctx.send(embed=em)
  

@bot.command()
async def help(ctx):
  em = discord.Embed(title = "LGBOT", description = "", color = 0x7d386f)
  em.add_field(name = "`>addquote <quote>`", value = "Adds your own quote to the random quote database! :)")
  em.add_field(name = "`>quote`", value = "Sends you a random quote!")
  em.add_field(name = "`>amount`", value = "Shows you the total amount of useless quotes y'all made")
  em.add_field(name = "`>cooldowns`", value = "The cooldown times for certain commands")
  em.add_field(name = "`>staff`", value = "Shows all staff")
  em.add_field(name = "`>leaderboard`", value = "Shows you the person that holds the record for the most boosts simultaneously active")
  em.add_field(name = "`>gif <search>`", value = "Sends a gay gif")
  em.add_field(name = "`>randomizers`", value = "Shows you all commands based on random generated values")
  em.set_footer(text = "Bot by Trainsgender") 
  await ctx.send(embed=em)

@bot.command()
async def leaderboard(ctx):
  em = discord.Embed(title = "Booster Leaderboard", description = "", color = 0x7d386f)
  em.add_field(name = ":first_place:", value = "Solar_xx#2895 - 7 boosts")
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)
               
@bot.command()
async def staff(ctx):
  em = discord.Embed(title = "LGBTeens Staff", description = "", color = 0x7d386f)
  em.add_field(name = "Zoë", value = "Server administrator, founder")
  em.add_field(name = "Emily", value = "Head moderator")
  em.add_field(name = "Joseph", value = "Moderator")
  em.add_field(name = "Max", value = "Moderator")
  em.add_field(name = "Tyler", value = "Moderator")
  em.add_field(name = "Fahad", value = "Moderator")
  em.add_field(name = "<insert pi name>", value = "Moderator")
  em.add_field(name = "Jax", value = "Helper")
  em.add_field(name = "Aubrey", value = "Helper")
  em.set_footer(text = "Bot by Trainsgender")
  await ctx.send(embed=em)             

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def addquote(ctx, *args):

  with open("data.json") as f:
    data = json.load(f) 

  for arg in args :
    with open("data.json") as f:
      data = json.load(f)

    data["quotes"].append('{}'.format(' '.join(args)))
  
    with open('data.json', 'w') as f:
      json.dump(data, f)
    await ctx.send('Your quote: "{}" is now saved and accessible with `>quote`!'.format(' '.join(args)))
    break
    

@addquote.error
async def addquote_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = "You're on cooldown! You have {:.2f} seconds left".format(error.retry_after)
    await ctx.send(msg)
  else:
    raise error

@bot.command()
async def amount(ctx):

  with open('data.json') as j:
   rq = json.load(j)
  
  var = len(rq["quotes"]) 

  await ctx.send(f"There are exactly {var} quotes in the database right now!")

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def quote(ctx):
  with open('data.json') as j:
   rq = json.load(j)
  
  await ctx.send('**"**' + random.choice(rq["quotes"]) + '**"**')

@quote.error
async def quote_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = "You're on cooldown! You have {:.2f} seconds left".format(error.retry_after)
    await ctx.send(msg)
  else:
    raise error

@bot.command()
async def cooldown(ctx):
  em = discord.Embed(title = "Cooldowns", description = "", color = 0x7d386f)
  em.add_field(name = "`>quote`", value = "10 seconds")
  em.add_field(name = "`>gif`", value = "10 seconds")
  em.add_field(name = "`>addquote`", value = "30 seconds")
  em.add_field(name = "`>whoiscuter`", value = "40 seconds")
  em.set_footer(text = "Bot by Trainsgender") 
  await ctx.send(embed=em)


bot.run(token)
