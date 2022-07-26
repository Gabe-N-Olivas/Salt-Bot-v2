# Comment guide # = regular comment ## = section #/# = end of section ### = note to dev/self
### This file has been approved for a stable release as of revision 2
# Last Modified 7/24/2022

if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")

import random, os, discord

from Backend import log

async def copypasta(ctx, txt):
    log.com(ctx)
    path = './Frontend/txt/pasta/'
    if txt == "list":
        await ctx.send(str(os.listdir(path)).replace(".txt", "")[1:-1]) 
    else:
        if txt == "rand" or txt == None:
            txt = os.listdir(path)
            oPath = (f"{path}{random.choice(txt)}")  # Selects a random element from the list
        else: oPath = (f"{path}{txt}.txt")

        try:
            with open(oPath, "r", encoding="utf8") as p:
                msg = "".join(p.readlines())
            await ctx.send(msg)
            del(msg)
            log.me(f"{path} was picked")
        except FileNotFoundError: 
            await ctx.send("That file doesn't exist!")
            log.me(f"User tried to open non-existent file '{path}'")
        except discord.errors.HTTPException:
            log.me(f"{path} is longer than 2000 words and unfortunately can not be sent by the bot")
            await ctx.send("That file doesn't exist")
        del(path)
    del(ctx, txt)

async def memeMe(ctx):
    log.com(ctx)
    path = './Frontend/img/'
    randImg = os.listdir(f'{path}RandMeme/')
    path = (f"{path}/{random.choice(randImg)}")  # Selects a random element from the list
    await ctx.send(file=discord.File(path))
    log.me(f"{path} was picked")
    del(ctx, randImg, path)

async def gato(ctx):
    log.com(ctx)
    path = './Frontend/img/'
    randImg = os.listdir(f'{path}gato/')
    path = (f"{path}{random.choice(randImg)}")  # Selects a random element from the list
    await ctx.send(file=discord.File(path))
    log.me(f"{path} was picked")
    del(ctx, randImg, path)

async def GOTM(ctx, link):
    log.com(ctx)
    await ctx.send(f"GOTM (Game Of The Month)\n\nSave Up your V-Bucks because every 20th day of the month the mods will be giving us a game to buy (<$30) and possibly play for the month\nThis month's game is: {link}")

async def slap(ctx, member):
    log.com(ctx)
    await ctx.send(f"{ctx.author.mention} has slapped <@{member.id}>!\nhttps://tenor.com/view/nope-stupid-slap-in-the-face-phone-gif-15151334")
    del(ctx, member)