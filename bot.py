# bot.py
# Last Modified 7/24/2022
# Comment guide # = regular comment ## = section #/# = end of section ### = note to dev/self 
### This file has been approved for a stable release as of revision 2

## Global python modules
 
###!    Goals for future versions: 

###TODO 2.1 add a .conf file to control setting from OUTSIDE the bot
###TODO 2.2 implement embeds
###TODO 2.3 add a console for direct access to commands 
###TODO 2.4 switch commands from prefix based to discords "/" commands

try:
    import discord
    from discord.ext import commands, tasks
    from typing import Union
except: raise ImportError("Import Error in bot.py : Discord.py not installed!\nYou can install it using \"pip install discord\"")

#/#



## Local python modules

#Essential Packages
try: from Backend import define, loggedOnly as lo, base as b, admin as a # All command/function focused modules will have an "as [x]" in order to simplify commands
except ImportError: raise ImportError("Import error in bot.py: One or more imports from the Backend Folder is missing!\nList of imports used: 'log'\nMake sure your install isn't corrupt or incomplete")

#Optional Packages
try: from Backend import game as g, fun as f, dev as d
except ImportError:
    run = input("Some Non critical packages are missing. This could cause instability if a user calls a function that doesn't exist.\nDo you want to load this script anyway? (Y/n)> ")
    if run != "Y": exit("Manual Halt")
    del(run) #run is no longer needed after this point

###



## Variables
# This reads the token file
try: token = open('t0ken.secret', 'r')
except: raise Exception("bot.py t0ken Error: Your token file could not be found!")

t0kenOF = 0 # Sets up our t0ken overflow variable for our for loop
for line in token: #t0ken should only have 1 line!!!
    t0k3n = line.rstrip("\n") 
    t0kenOF = t0kenOF + 1 #counts the lines in your token file

if t0kenOF != 1: raise Exception("bot.py t0ken Error: Your t0ken file is not valid!\nMaybe you have more than one line in your file?") #If your t0ken file is not 1 line then the program will not run
else: del(t0kenOF) # After this point t0ken overflow will not be needed

v = "2.0.Stable"

if v.startswith("Beta"): devmode = True # This enables dev testing while the bot is still in beta
else: devmode = False
global prfx
prfx = "$" # This alone does not set the prefix (that is defined in define.py) but allows the bots functions to know what prefix is used
bot = define.bot # This is the bots "config" file and sets the defaults for the bot such as case insensitivity, prefixes, intents, etc...
#/#



## Base Commands

@bot.event # Remember bot.events have predefined async definitions so don't make up your own
async def on_ready():
    await b.boot(prfx, v)

@bot.event
async def on_member_join(member): 
    await b.newMember(member)

@bot.command(name='test', help='test the bot') # "name" is the word that needs to be invoked for a command to run "help" is what displays when a user uses the help command
async def test(ctx):
    await b.test(ctx)

@bot.command(name="privacypolicy", help="Links to the TOS & Privacy Policy")
async def privacyPolicy(ctx):
    await b.privacyPolicy(ctx)

@bot.command(name="about", help="Shows you what version you are running")
async def about(ctx):
    await b.about(ctx, v)

@bot.command(name="ping", help="Tests the latency between you and the server")
async def ping(ctx):
    await b.ping(ctx)

@bot.command(name="pingme", help=f"Set a time to ping you | pingme (number) (ms, sec, min, hour, day)")
async def pingMe(ctx, timeAmnt, timeUnit):
    await b.pingMe(ctx, timeAmnt, timeUnit)

@bot.command(name='pingmod', help='Pings the mods for help')
async def pingMod(ctx):
    await b.pingMod(ctx)

@bot.command(name='credstat', help=f'Shows you or another person credit score| credstat (user)[optional]')
async def credStat(ctx, member: discord.Member = None):
    await b.credStat(ctx, member)

@bot.command(name='avatar', help=f'fetch a users profile picture | avatar (user)')
async def avatar(ctx, member: discord.Member):
    await b.avatar(ctx, member)

@bot.command(name="big", help=f"Makes an emoji bigger! | big (emoji)")
async def big(ctx, emoji: Union[discord.Emoji, str] = None):
    await b.big(ctx, emoji)

#/#



## Game
@bot.command(name="rps", help="Play a game of Rock, Paper, Scissors!")
async def RPS(ctx):
    await g.RPS(ctx)

@bot.command(name="randmath", help="Play a quick math game!")
async def randMath(ctx):
    await g.randMath(ctx)

#/#



## Fun

@bot.command(name='copypasta', help=f'Gets a copypasta for your reading pleasure | copypasta (name)[You can do rand for a random copypasta or "list" to show a list of copypastas]')
async def copypasta(ctx, type = None):
    await f.copypasta(ctx, type)

@bot.command(name='mememe', help='Get an image from a curated list!')
async def memeMe(ctx):
    await f.memeMe(ctx)

@bot.command(name="gato", help = "gato maker")
async def gato(ctx):
    await f.gato(ctx)

@bot.command(name="slap", help = f"slap a person! | slap (user)")
async def fap(ctx, member : discord.Member):
    await f.slap(ctx, member)

#/#



## ADMIN ONLY COMMANDS
@bot.command(name="credit", help=f"Gives members credit if they give out good posts | credit (+number, -number) (member) (Reason)[optional]")
@commands.has_role('BotAuth')
async def credit(ctx, credit, member : discord.Member, *, reason = None):
    await a.credit(ctx, credit, member, reason)

@bot.command(name="purge", help=f"Clears up to 20 messages | purge (amount)")
@commands.has_role('BotAuth')
async def purge(ctx, amount):
    await a.purge(ctx, amount)

@bot.command(name="mute", help=f"Mutes a user | mute (user)")
@commands.has_role('BotAuth')
async def mute(ctx, member : discord.Member):
    await a.mute(ctx, member)

@bot.command(name="unmute", help=f"UNmutes a user | unmute (user)")
@commands.has_role('BotAuth')
async def unmute(ctx, member: discord.Member):
    await a.unmute(ctx, member)

@bot.command(name="ban", help=f"Bans a user | ban (member) (Reason)[optional]")
@commands.has_role('BotAuth')
async def ban(ctx, member : discord.Member, *, reason = None):
    await a.ban(ctx, member, reason)

#/#    

## Developer commands (DELETE THIS IF THIS BOT IS TO BE USED IN MORE THAN 1 SERVER!)

@bot.command(name="devmode")
@commands.has_role('Dev')
async def devmodeSet(ctx, TorF = None):
    global devmode
    devmode = await d.devmode(ctx, TorF, devmode)

@bot.command(name='testlog')
@commands.has_role('Dev')
async def testLog(ctx):
    await d.testLog(ctx, devmode)

@bot.command(name="forcetraceback")
@commands.has_role('Dev')
async def forceTraceback(ctx):
    await d.forceTraceback(ctx, devmode)

@bot.command(name="prfxchng")
@commands.has_role('Dev')
async def prfxChng(ctx, prfxChng):
    global prfx
    prfx = await d.prfxChng(ctx, prfx, prfxChng, devmode)

@bot.command(name="refresh")
@commands.has_role('Dev')
async def refresh(ctx):
    await d.refresh(ctx, devmode, prfx)

@bot.command(name='toggle')
@commands.has_role('Dev')
async def toggle(ctx, command):
    await d.toggle(ctx, devmode, command)

### This doesn't seem to work disable on Stable Release
#!#@bot.command(name="rs")
#!#@commands.has_role('Dev')
#!#async def restart(ctx):
#!#    await d.restart(ctx, devmode)

@bot.command(name='sh')
@commands.has_role('Dev')
async def shutdown(ctx):
    await d.shutdown(ctx, devmode)

## Logged Only events

@bot.event
async def on_guild_join(guild):
    await lo.serverConnect(guild)

@bot.event
async def on_guild_remove(guild):
    await lo.serverDisconnect(guild)

@bot.event
async def on_command_error(ctx, error):
    await lo.ErrCatch(ctx, error, prfx)

@tasks.loop(hours=24)
async def deleteLog():
    lo.deleteLog()

#/#



##TOKEN used to run bot

bot.run(t0k3n)

#/#
