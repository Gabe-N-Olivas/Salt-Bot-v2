# Comment guide # = regular comment ## = section #/# = end of section ### = note to dev/self
### This file has been approved for a stable release as of revision 2
# Last Modified 7/24/2022

if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")

try: from discord.ext import commands
except ImportError: raise ImportError("Import error in loggedOnly.py: One or more imports are missing!\nList of imports used: 'discord'\nTry updating or installing these with pip")

try: from Backend import log
except ImportError: raise ImportError("Import error in loggedOnly.py: One or more imports from the Backend Folder is missing!\nList of imports used: 'log'\nMake sure your install isn't corrupt or incomplete")

try: import conf as c
except: 
    try:
        from Backend import log
        log.me("conf.py failed to load!")
        print("WARNING 'conf.py' NOT FOUND! Falling back to 'defcon.py'"); from Backend import defcon as c
    except ImportError: 
        raise Exception("Failed to load both 'conf.py' and 'defcon.py'!"); exit("Config files could not be properly loaded")

async def serverConnect(guild): # when the bot enters a new server it logs it
    log.me(f"Bot has joined {guild}")

async def serverDisconnect(guild): # when the bot's connection to a server ends (I.E. it gets removed, banned, or kicked) it logs it
    log.me(f"Bot no longer has connection to {guild}")

async def ErrCatch(ctx, error, prfx): # This is what catches errors and prints it
    import sys
    import traceback
    if isinstance(error, commands.errors.CheckFailure): # Triggers if a user does not have BotAuth(or other mod role)
        log.me(f"{ctx.message.author} in {ctx.message.channel} tried to use the admin command: '{ctx.command}'")
        await ctx.send("You dont have permission to do that. If you think this is an error message the mods\nIf you are an admin this command requires a role called 'BotAuth' without quotes")
    elif isinstance(error, commands.DisabledCommand): # Triggers if a user invokes a disabled command
        log.me(f"{ctx.message.author} in {ctx.message.channel} tried to use the disabled command: '{ctx.command}'")
        await ctx.send(str(ctx.command) + " has been disabled.")
    elif isinstance(error, commands.MissingRequiredArgument): # Triggers if a user had a missing argument
        log.me(f"{ctx.message.author} in {ctx.message.channel} had a missing argument when using command: '{ctx.command}'")
        await ctx.send(f"You seem to be missing an argument! See how this command works by using {prfx}help {ctx.command}")
    elif isinstance(error, commands.BadArgument): # Triggers if a user had a bad argument
        log.me(f"{ctx.message.author} in {ctx.message.channel} had a bad argument when using a command when using {ctx.command}")
        await ctx.send(f"Your command seems to have a bad argument use {prfx}help {ctx.command} for valid uses of this command")
    elif isinstance(error, commands.CommandNotFound): # Triggers if a user try's invoking a command that doesn't exist
        log.me(f"{ctx.message.author} in {ctx.message.channel} tried to use a non-existent command: {ctx.command}")
        await ctx.send(f":/ That command doesn't exist use {prfx}help to see all commands!")
    elif isinstance(error, commands.TooManyArguments): # Triggers if a user had TOO many arguments
        log.me(f"{ctx.message.author} in {ctx.message.channel} used too many arguments using {ctx.command}")
        await ctx.send(f"WOAH too many arguments! Use {prfx}help {ctx.command} to find out how to use this")
    else: # This catches all other errors and prints them to the terminal and to the log file
        await ctx.send("Hmmm..." + str(ctx.command) + " didn't work!")
        log.me(f"{ctx.command} didn't work! Traceback below")
        log.me(f'Ignoring exception in command {ctx.command}:')
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        tb = tb.split('The above exception was the direct cause of the following exception:', 1)[0]
        log.me(tb) ### Command does not work in linux
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        print(f"{error}")
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

async def deleteLog():
    from datetime import datetime
    import os
    now = datetime.now()
    time = now.strftime("%d")
    if time == 1: 
        try: os.remove("log")
        except: log.me("Log Created\nThis file was made because deleteLog tried to delete a non-existent log")