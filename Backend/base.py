# Comment guide # = regular comment ## = section #/# = end of section ### = note to dev/self
### This file has been approved for a stable release as of revision 2
# Last Modified 7/24/2022

###TODO Add an image embedding system (i.e. $image (url) and this would show any web image/video in an embed)

if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")

try: import discord, json, asyncio
except ImportError: raise ImportError("Import error in base.py: One or more imports are missing!\nList of imports used: 'discord', 'json', 'asyncio'\nTry updating or installing these with pip")

try: from Backend import log, define
except ImportError: raise ImportError("Import error in base.py: One or more imports from the Backend Folder is missing!\nList of imports used: 'log'\nMake sure your install isn't corrupt or incomplete")

bot = define.bot

#This function takes a number followed by a unit and converts it ito its real time measure (i.e 1 min to 60 sec)
def realtime(timeAmnt, timeUnit):
    if timeUnit == "sec": timeAmnt = timeAmnt # this changes nothing
    elif timeUnit == "min": timeAmnt = timeAmnt*60 # this converts into minutes
    elif timeUnit == "hour": timeAmnt = timeAmnt*3600 # this converts into hours
    elif timeUnit == "day": timeAmnt = timeAmnt*86400 # this converts into days
    else: timeAmnt = None # If the user enters a non-existent option then this returns None
    return(int(timeAmnt))

async def boot(prfx, v):
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"Use {prfx}"))
    
    # Send to console
    print("Bot has logged into server")
    print(f"{bot.user.name} {v} has booted up and is ready to use") # displays the bots name
    print(f"\n{'#'*60}\n(Linux Only) To run me in the background\nPress Ctrl+Z\nType in bash bg (restart the process in the background\nthen disown %1 (assuming this is job #1, use jobs to determine)\n{'#'*60}") # displays information on how to run this in the background
    
    log.me(f"{bot.user.name} {v} has come online!")
    
    del(prfx, v)

async def newMember(member): 
    guild = str(member.guild.name)
    
    msg = "Have Fun!"
    
    # Attempts to contact the user
    try: await member.create_dm(); await member.dm_channel.send(f'Hi {member.name}, welcome to {guild}! {msg}')
    # If the user can not be DMed it just gets logged
    except: log.me(f"{member} could not be DMed")
    
    # Attempts to add a user to the credit system
    try:
        with open('../txt/credit.json', 'r') as f: users = json.load(f)
    # If the credit.json can not be found it logs this error to the console
    except: log.me(f"{member.name} could not be added to credit system as it doesn't exist"); raise Exception("newMember in admin.py Error: credit.json doesn't seem to exist!\n If it's missing, create a new file in ../txt/ and name it credit.json")

    # Only adds new members to avoid conflicts with two different credit scores for the same user
    if not f'{member.id}' in users:
        users[f'{member.id}'] = {}
        users[f'{member.id}']['credit'] = 0
        log.me(f"{member.name} was DMed when they joined a server\nThey also were added to the credit system")
    else: log.me(f"{member.name} was DMed when they joined a server\nThey were already in the credit system")
    # When all is finished it saves the data to the credit.json file
    with open('../txt/credit.json', 'w') as f: json.dump(users, f)

    del(guild, msg, f, member)

async def test(ctx):
    log.com(ctx)

    await ctx.send(f"This is the test of the <@{bot.user.id}>") # Gets the bot's user id to be usable on different bots
    
    del(ctx)

async def privacyPolicy(ctx):
    log.com(ctx)

    await ctx.send("") # Edit this with your Privacy Policy
    
    del(ctx)

async def about(ctx, v):
    log.com(ctx)
    
    #try: await ctx.send(file=discord.File(f"Frontend/MOTV{v}.png")) #Tries to find MOTV and make sure it's the correct version
    #except: log.me("Frontend MOTV missing! Maybe your using an old version of MOTV?") 
    # Writing these two blocks separate makes sure that the text is at least sent even if the MOTV file is missing
    await ctx.send(f"This is SaltBOT {v}\nThis bot was created by Gabe-N-Olivas\nThis work is licensed under the GNU General Public License v2. \nThe official repository for SaltBOT is located at https://drive.google.com/drive/u/0/folders/1GgQM5R66Di8BkhZEB-81LSLcIWJWpk5d")

    del(ctx)

async def ping(ctx):
    log.com(ctx)

    ping = round((bot.latency*1000)) # Rounds out the number and changes the number to ms
    
    if ping < 100: await ctx.send(f"Pong! Response times are great! Ping is: {ping} ms") # Each one of these levels tells the user what to expect in terms of latency
    elif ping < 200: await ctx.send(f"Pong! Response times are good! Ping is: {ping} ms")
    elif ping < 500: await ctx.send(f"Pong! Response times are fair. Ping is: {ping} ms\nThe Bot may be somewhat unresponsive")
    elif ping < 1000: await ctx.send(f"Pong! Response times are poor. Ping is: {ping} ms\nThe bot will be unresponsive at times")
    elif ping > 1000: await ctx.send(f"Pong! Response times are bad! Ping is: {ping} ms\nThe bot will be unresponsive most of the time") # I don't think this will ever show up because ping times that high usually cause nothing to work

    del(ctx, ping)

async def pingMe(ctx, timeAmnt, timeUnit):
    log.com(ctx)

    try: int(timeAmnt) # Attempts to convert inputted number to a integer
    except ValueError: await ctx.send("You need to use a whole number for time amount!"); return # Triggers on decimal input
    except: await ctx.send("Time amount isn't a number!"); return # Triggers on a non int input
    
    await ctx.send(f"Okay, you got it! In {timeAmnt}{timeUnit}(s) I'll ping you!") # Lets the user know when they will be pinged
    
    try: 
        log.me(f"This user set the timer for {timeAmnt}{timeUnit}(s)")
        await asyncio.sleep(realtime(timeAmnt, timeUnit)) # You MUST use asyncio.sleep and not time.sleep because it will just halt the program
        await ctx.send(f"{ctx.author.mention} TIMES UP! That was {timeAmnt}{timeUnit}(s)")
    except: await ctx.send("That isn't a valid time format! Valid Args: (ms, sec, min, hour, day)") # This triggers if someone uses an invalid arg for timeUnit where it does not exist in realtime()
    
    del(ctx, timeAmnt, timeUnit)

async def pingMod(ctx):
    log.com(ctx)

    try: 
        mod = discord.utils.get(ctx.guild.roles, name='BotAuth') # Attempt to get BotAuth role id
        await ctx.send(f"{mod.mention}! {ctx.author.mention} has pinged you!") # Mentions all mods with BotAuth role
    except AttributeError: await ctx.send("There is no BotAuth role!(Note for admins: you must give yourself a role named BotAuth for admin commands to work)") # Triggers if there is no BotAuth Role

    del(ctx, mod)

async def credStat(ctx, member):
    log.com(ctx)

    try:
        if member == None: id = ctx.message.author.id # If there is no pinged user then it defaults to the user that invoked the command
        else: id = member.id # If some one was pinged then it tries to get their id
    except: await ctx.send("That isn't a valid user!"); return # If the user mentioned isn't a user then it returns that to the end-user
    
    try: 
        with open('../txt/credit.json', 'r') as c: users = json.load(c) # reads the credit.json file
        del(c)
    except: raise FileNotFoundError("credStat in base.py Error: credit.json doesn't seem to exist!\n If it's missing, create a new file in ../txt/ and name it credit.json")
    
    try: 
        credit = users[str(id)]['credit'] # finds the credit amount
        await ctx.send(f'<@{id}> credit level is {credit}!')
        del(users, credit)
    except KeyError: await ctx.send("That user isn't in the credit system!")
    

    del(ctx, member, id)
    

async def avatar(ctx, member):
    log.com(ctx)

    if not member: await ctx.send(f"Could not find {member}"); return # Triggers if the bot can not find member or members profile picture
    pfp = member.avatar_url # sets pfp to the member's profile picture
    embed=discord.Embed(title=f"{member}'s", description='Profile Picture'.format(member.mention) , color=0xecce8b) #creates an embed for eye candy
    embed.set_image(url=(pfp)) # sets the embedded image to the member's profile picture
    await ctx.send(embed=embed) # finally sends the embed
    
    log.me(f"This user fetched {member}'s profile picture")
    
    del(ctx, member, embed, pfp)

async def big(ctx, emoji):
    log.com(ctx)
    
    # custom emoji
    embed=discord.Embed(title=str(emoji), color=0xf1c40f) 
    if isinstance(emoji, discord.Emoji): #checks to see if it's a custom discord emoji
        embed.set_image(url=(emoji.url)) # Gets the url of the emoji image
        await ctx.send(embed=embed)
    
    # default emoji
    elif isinstance(emoji, str):
        import requests
        url=f"https://twemoji.maxcdn.com/v/latest/72x72/{ord(emoji[0]):x}.png"
         # Gets the url of the emoji image from the twemoji cdn
        if requests.get(url).status_code == 404: 
            log.me(f"This user tried to use a non existent or nitro emoji URL: {url}")
            await ctx.send(embed=discord.Embed(title="That's Not A Valid Emoji...", color=0xc0392b))
        else:
            embed.set_image(url=url) 
            await ctx.send(embed=embed)
        del(url)

    del(ctx, emoji, embed)