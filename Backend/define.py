# Comment guide # = regular comment ## = section #/# = end of section ### = note to dev/self
### This file has been approved for a stable release as of revision 2
# Last Modified 7/24/2022

if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")
try:
    import discord
    from discord.ext import commands
except ImportError: raise ImportError("Import error in define.py: One or more imports are missing!\nList of imports used: 'discord', 'json', 'asyncio'\nTry updating or installing these with pip")

try: import conf as c
except: 
    try:
        from Backend import log
        log.me("conf.py failed to load!")
        print("WARNING 'conf.py' NOT FOUND! Falling back to 'defcon.py'"); from Backend import defcon as c
    except ImportError: 
        raise Exception("Failed to load both 'conf.py' and 'defcon.py'!"); exit("Config files could not be properly loaded")

#Enabling discords "intents"
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.reactions = True
intents.members = True

#defines bot commands using the prefix $ for actuation
bot = commands.Bot(command_prefix="$", intents=intents, case_insensitive=c.commandCaseInsensitivity)