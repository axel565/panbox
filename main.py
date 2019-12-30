import discord,os
import asyncio
from discord.ext import commands 

bot = commands.Bot(command_prefix='ay ') 

@bot.event
async def on_ready():
    game = discord.Activity(name="Under Development", type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.dnd, activity=game)
   
@bot.command() 
async def say(ctx,*,args):
    await ctx.send(args) 
    await ctx.message.delete()
@bot.command() 
async def hi(ctx):
    user = ctx.author
    await ctx.send("Hello "+str(user)) 

@bot.command() 
async def dothis(ctx):
    await ctx.send("Done :sunglasses:")
@bot.group() 
async def ign(ctx):
    await ctx.send("No IGN yet")
@ign.command
async def add(ctx,*,inp):
    await ctx.send("Your IGN : "+str(inp))
 

bot.run(os.getenv('token'))