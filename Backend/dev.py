# Comment guide # = regular comment ## = section #/# = end of section ### = note to dev/self
### This file has been approved for a stable release as of revision 2
# Last Modified 7/24/2022

if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")


try: import discord, asyncio
except ImportError: raise ImportError("Import error in dev.py: One or more imports are missing!\nList of imports used: 'discord', 'asyncio'\nTry updating or installing these with pip")

try: from Backend import log, define
except ImportError: raise ImportError("Import error in dev.py: One or more imports from the Backend Folder is missing!\nList of imports used: 'log'\nMake sure your install isn't corrupt or incomplete")

bot = define.bot

async def devmode(ctx, TorF, devmode):
    try: from passlib.hash import bcrypt
    except ImportError: 
        await ctx.send("This command can not be used due to unknown error")
        log.me("Passlib not installed! Install it to make dev commands work!"); return

    log.com(ctx)

    try: hash = open("./Backend/hash", "r")
    except: await ctx.send("Devmode has been disabled by your bot maintainer"); return # If the hash file is not found it is assumed that the dev does not want devmode to be enabled
    hashOF = 0 #Hash Overflow
    
    # Opens and reads the hash file
    for hsh in hash: hash = hsh.rstrip("\n"); hashOF = hashOF + 1
    if hashOF != 1: 
        del(hashOF)
        raise Exception("devmode in dev.py Error: The hash file is corrupt! Devmode not set") # If the hash has more than one line then it is not valid
    
    hasher = bcrypt.using(rounds=12) # The default hash uses 12 rounds for the best blend of speed and security
    
    check = lambda m: m.author == ctx.author #Checks if the person responding is the message author

    await ctx.send(f"!!!Before you can access Devmode you need to enter the devmode password!!!\nRemember to do this in a private channel! If this channel is not private let this command time out and do it in a private channel")
    try:
        password = await bot.wait_for(event="message", check=check, timeout=15)
        await ctx.channel.purge(limit=1) # THIS IS NOT 100% SECURE! IF YOU USE THIS IN A PUBLIC CHANNEL YOUR PASSWORD WILL BE LEAKED! THIS IS BECAUSE THE PURGE COMMAND HAS A DELAY
        if hasher.verify(password.content, hash) == True: # Checks if the hash of the message and the hash stored in hash are the same
            del(password) # First thing you should do is remove password from memory
            if TorF == "True": await ctx.send("Devmode on, play with this at your own risk..."); devmodeR = True; log.me(f"devmode was set to {TorF}")
            elif TorF == "False": await ctx.send("Devmode disabled!"); devmodeR = False; log.me(f"devmode was set to {TorF}")
            else: await ctx.send("Devmode not set, bad argument given Valid arguments: (True, False)"); devmodeR = devmode # If a bad arg is given, a timeout error is given, or the incorrect password is set devmode stays the same.
        else: del(password); await ctx.send("Invalid Password! Devmode not set."); devmodeR = devmode
    except asyncio.TimeoutError: await ctx.send("TimeOut Error!"); devmodeR = devmode
    del(ctx, TorF, devmode, hash, hasher, check)
    return(devmodeR)

# This function just helps save time use it when making a new dev function
async def check4dev(ctx, devmode):
    if devmode == True: del(ctx, devmode); return(True)
    elif devmode == False:
        await ctx.send("Devmode not enabled, no changes have been made")
        log.me(f"Devmode command \"{ctx.command}\" was executed by {ctx.message.author} when devmode was set to false")
        del(ctx, devmode)
        return(False)
    else:
        await ctx.send(f"Devmode is not set to either True or False! Please check any source code modifications!\nCurrent Devmode state = {devmode}\nFalling back to state False")
        del(ctx, devmode)
        return(False)
    
#This makes it easier to call this function even if it is a bit redundant
c4d = check4dev

async def testLog(ctx, devmode):
    if await c4d(ctx, devmode) == True:
        log.com(ctx) #log commands must be placed in the if statement or else a command will be logged twice because of check4dev
        await ctx.send("This should have saved to the log")
        log.me(f"{ctx.message.id}, 𝔗 (Fancy T), 😊 (Emoji), ‱ (Special Math Symbol), ※ ௹ ⨌ (Unicode Symbols), Ὥ(Greek Symbol) This should have been saved perfectly with no boxes") # This provides the encoding engine different characters to process
    del(ctx)

async def forceTraceback(ctx, devmode):
    if await c4d(ctx, devmode) == True:
        log.com(ctx)
        await ctx.send("Traceback sent see log\nIf you see a message saying traceback didn't work that means that it did work")
        0 + "traceback" # This will clearly be a problem and hopefully be logged
    del(ctx, devmode)

async def prfxChng(ctx, prfxChng, devmode):
    if await c4d(ctx, devmode) == True:
        log.com(ctx)
        await ctx.send(f"Your server prefix has been changed to {prfxChng}")
        bot.command_prefix = prfxChng # This is what truly sets the bot's prefix
        log.me(f"The prefix was changed to {prfxChng}")
        return(prfxChng)
    del(ctx, devmode)

def prfxChngSet(prfx, prfxChng, devmode):
    if devmode == True: prfxR = prfxChng # This is just to update the variable prfx it does NOT set the actual prefix
    else: prfxR = prfx # Sets the prefix to the same as before
    del(prfx, prfxChng, devmode)
    return(prfxR)

async def refresh(ctx, devmode, prfx):
    if await c4d(ctx, devmode) == True:
        log.com(ctx)
        await ctx.send("Refreshing")
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"Use {prfx}, If I mess up let my maintainer @ape#3847 know")) # Resets the bots status
    del(ctx, devmode, prfx)

async def toggle(ctx, devmode, command):
    if await c4d(ctx, devmode) == True:
        log.com(ctx)

        command = bot.get_command(command)
        if command == None:
            await ctx.send("That command doesn't exist!"); return
        
        stateToBe = "disabled" if command.enabled else "enabled" # Checks if the command is currently enabled and if it is, it reports the state it will be after execution to be enabled to be disabled
        await ctx.send(f"Command: {command}, will be {stateToBe}\nAre you sure you want to execute? (Y/n)")
        
        check = lambda m: m.author == ctx.author
        try:
            msg = await bot.wait_for(event="message", check=check, timeout=15)
            if msg.content == "Y":
                command.enabled = not command.enabled # Changes the command state
                await ctx.send(f"{command} has been {stateToBe}") # Provides conformation that the command has been disabled
                log.me(f"Command {command} was {stateToBe} by {ctx.message.author}")
            else: await ctx.send("No action has been taken") # Provides conformation that the command has NOT been disabled
        except asyncio.TimeoutError: await ctx.send("TimeOut Error!")
        del(command, check, msg, stateToBe)
    del(ctx, devmode)
        
### This doesn't seem to work so it's disabled on the Stable Release
#//async def restart(ctx, devmode):
#//    if await c4d(ctx, devmode) == True:
#//        import os
#//        import sys
#//        await ctx.send("Restarting...")
#//        log.com(ctx)
#//        os.system("clear")
#//        os.execv(sys.executable, ['python'] + sys.argv)

async def shutdown(ctx, devmode):
    if await c4d(ctx, devmode) == True:
        log.com(ctx)
        await ctx.send("Shutting down...")
        exit("Exit initiated from bot command") # Shuts everything down
