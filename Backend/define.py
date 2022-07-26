# Comment guide # = regular comment ## = section #/# = end of section ### = note to dev/self
### This file has been approved for a stable release as of revision 2
# Last Modified 7/24/2022

if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")
try:
    import discord
    from discord.ext import commands
except ImportError: raise ImportError("Import error in define.py: One or more imports are missing!\nList of imports used: 'discord', 'json', 'asyncio'\nTry updating or installing these with pip")
#Enabling discords "intents"
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.reactions = True
intents.members = True

#defines bot commands using the prefix $ for actuation
bot = commands.Bot(command_prefix="$", intents=intents, case_insensitive=True)