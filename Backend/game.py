# Comment guide # = regular comment ## = section #/# = end of section ### = note to dev/self
### This file has been approved for a stable release as of revision 2
# Last Modified 7/24/2022

if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")

try: import random, asyncio
except ImportError: raise ImportError("Import error in game.py: One or more imports are missing!\nList of imports used: 'discord', 'asyncio'\nTry updating or installing these with pip")

try: from Backend import define, log
except ImportError: raise ImportError("Import error in game.py: One or more imports from the Backend Folder is missing!\nList of imports used: 'log'\nMake sure your install isn't corrupt or incomplete")

try: import conf as c
except: 
    try:
        from Backend import log
        log.me("conf.py failed to load!")
        print("WARNING 'conf.py' NOT FOUND! Falling back to 'defcon.py'"); from Backend import defcon as c
    except ImportError: 
        raise Exception("Failed to load both 'conf.py' and 'defcon.py'!"); exit("Config files could not be properly loaded")

bot = define.bot

async def RPS(ctx):
    log.com(ctx)
    from .game_assets import RPS_Assets
    await ctx.send("Rock, Paper, Scissors!\n(Type either Rock, Paper, Scissors to play!)")
    check = lambda m: m.author == ctx.author
    try:
        options = ("rock", "paper", "scissors")
        gen = random.choice(options)
        msg = await bot.wait_for(event="message", check=check, timeout=15)
        inp = msg.content.lower()
        await RPS_Assets.RPS(ctx, options, gen, inp)
    except asyncio.TimeoutError:
        await ctx.send("TimeoutError!: You took too long!")
    del(ctx, check, options, gen, msg, inp)

async def randMath(ctx):
    log.com(ctx)
    from .game_assets import RM_Assets
    check = lambda m: m.author == ctx.author
    try:
        await ctx.send("What mode would you like to do? Easy, Hard, Nightmare")
        difficulty = await bot.wait_for(event="message", check=check, timeout=10)
        try:
            await RM_Assets.randNum(ctx, difficulty.content.lower())
            ans = await bot.wait_for(event="message", check=check, timeout=10)
            await RM_Assets.display(ctx, ans.content)
            await RM_Assets.cleanup()
        except asyncio.TimeoutError:
            await ctx.send("FAILED: YOU TOOK TOO LONG")
            await RM_Assets.timeoutAns(ctx)
    except asyncio.TimeoutError:
        await ctx.send("TimeoutError!: You took too long!")

    del(ctx, check)
