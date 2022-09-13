# Comment guide # = regular comment ## = section #/# = end of section ### = note to dev/self
### This file has been approved for a stable release as of revision 2
# Last Modified 7/24/2022

if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")

import random, os, discord

from Backend import log

try: import conf as c
except: 
    try:
        from Backend import log
        log.me("conf.py failed to load!")
        print("WARNING 'conf.py' NOT FOUND! Falling back to 'defcon.py'"); from Backend import defcon as c
    except ImportError: 
        raise Exception("Failed to load both 'conf.py' and 'defcon.py'!"); exit("Config files could not be properly loaded")

async def copypasta(ctx, txt):
    log.com(ctx)
    path = './Frontend/txt/pasta/'
    if txt == "list":
        await ctx.send(str(os.listdir(path)).replace(".txt", "")[1:-1]) 
    else:
        if txt == "rand" or txt == None:
            txt = os.listdir(path)
            oPath = (f"{path}{random.choice(txt)}")  # Selects a random element from the list
        else: oPath = (f"{path}{txt.lower()}.txt")

        try:
            with open(oPath, "r", encoding="utf8") as p:
                msg = "".join(p.readlines())
            await ctx.send(msg)
            del(msg)
            log.me(f"{path} was picked")
        except FileNotFoundError: 
            await ctx.send("That file doesn't exist!")
            log.me(f"User tried to open non-existent file '{oPath}'")
        except discord.errors.HTTPException:
            log.me(f"{path} is longer than 2000 words and unfortunately can not be sent by the bot")
            await ctx.send("That file doesn't exist")
        del(path, oPath)
    del(ctx, txt)

async def memeMe(ctx):
    log.com(ctx)
    randImg = os.listdir(f'./Frontend/img/RandMeme/')
    path = (f"./Frontend/img/RandMeme/{random.choice(randImg)}")  # Selects a random element from the list
    try: await ctx.send(file=discord.File(path))
    except discord.HTTPException:
        await ctx.send("Whoops! The file i choose was too big. Try again")
        log.me(f"File:{path} is too large to be sent")
    log.me(f"{path} was picked")
    del(ctx, randImg, path)

async def gato(ctx):
    log.com(ctx)
    randImg = os.listdir(f'./Frontend/img/gato/')
    path = (f"./Frontend/img/gato/{random.choice(randImg)}")  # Selects a random element from the list
    await ctx.send(file=discord.File(path))
    log.me(f"{path} was picked")
    del(ctx, randImg, path)

async def slap(ctx, member):
    ###TODO Add local image source
    ###TODO maybe add a reaction system where users can duel?
    log.com(ctx)
    await ctx.send(f"{ctx.author.mention} has slapped <@{member.id}>!\nhttps://tenor.com/view/nope-stupid-slap-in-the-face-phone-gif-15151334")
    del(ctx, member)