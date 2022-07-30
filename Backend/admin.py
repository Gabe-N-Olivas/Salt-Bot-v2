# Comment guide # = regular comment ## = section #/# = end of section ### = note to dev/self
### This file has been approved for a stable release as of revision 2
# Last Modified 7/24/2022

from dis import disco

from attr import Attribute


if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")

try: import json, discord
except ImportError: raise ImportError("Import error in admin.py: One or more imports are missing!\nList of imports used: 'discord', 'json'\nTry updating or installing these with pip")

try:
    #Local Imports
    from Backend import log
except ImportError: raise ImportError("Import error in admin.py: One or more imports from the Backend Folder is missing!\nList of imports used: 'log'\nMake sure your install isn't corrupt or incomplete")

### Is this needed now that credit automatically adds users? Leave in for V2.S remove in 2.1
async def createCredit(ctx, member): #Adds a user to the credit system
    log.com(ctx)
    try:
        with open('./Frontend/txt/credit.json', 'r') as f: users = json.load(f) #Opens the JSON file Credit and assigns it to f / #Loads our data and assigns it to users
    except: raise FileNotFoundError("createCredit in admin.py Error: credit.json doesn't seem to exist!\nIf it's missing, create a new file in ./Frontend/txt/ and name it credit.json") # If the credit.json file is missing then the bot reports to the console on a quick fix

    if not f'{member.id}' in users: #Checks if the user isn't in the credit system
        users[f'{member.id}'] = {} #Encases the user id in curly brackets for formatting purposes
        users[f'{member.id}']['credit'] = 0 #Sets credit to 0
        await ctx.send("User has been added to system!") # Reports back that this operation was successful
        log.me(f"{member} was added to credit system")
    else: await ctx.send("User already in system!") #If the user is already in system then it outputs a notification to the admin
        
    with open('./Frontend/txt/credit.json', 'w') as f: #Opens the JSON file Credit and assigns it to f
        json.dump(users, f) #Dumps or information into the Credit file

    del(f, users ,member, ctx)

async def credit(ctx, credit, member, reason):
    log.com(ctx)
        
    try: credit = int(credit) #stops non ints from being added to the system
    except ValueError: await ctx.send("You need to use a whole number for time amount!"); return # Triggers on decimal input
    except: await ctx.send("Time amount isn't a number!"); return # Triggers on a non int input
    
    try:
        with open('./Frontend/txt/credit.json', 'r') as f: users = json.load(f)  #Opens the JSON file Credit and assigns it to f / #Loads our data and assigns it to users
    except: raise FileNotFoundError("credit in admin.py Error: credit.json doesn't seem to exist!\nIf it's missing, create a new file in ./Frontend/txt/ and name it credit.json") # If the credit.json file is missing then the bot reports to the console on a quick fix
    
    try: users[f'{member.id}']['credit'] += credit # writes credit amount to the user and selected user ID 
    except KeyError: 
        await ctx.send(f"That user doesn't exist in the credit system! Attempting to add them to credit system...") # If the user doesn't exist then it reports back how to add them to credit system
        await createCredit(ctx, member) # Invokes createCredit to add a user to credit.json
        await ctx.send("Success! Writing information...")
        with open('./Frontend/txt/credit.json', 'r') as f: users = json.load(f) # Reloads credit.json
        users[f'{member.id}']['credit'] += credit # writes credit amount to the user and selected user ID

    
    if credit > 0: await ctx.send(f"Good Job {member} you gained {credit} credit(s)!")
    elif credit < 0: await ctx.send(f"Uh Oh {member} you lost {credit} credit(s)!")
    else: await  ctx.send(f"Hmmm looks like your credit stays the same...")
    
    with open('./Frontend/txt/credit.json', 'w') as f: json.dump(users, f) # If all is successful the credit is written to the .json file 

    if reason != None: await ctx.send(f"Reason: {reason}") # Repeats message echoed by an admin

    log.me(f"{member} credit status changed by {credit}")

    del(credit, ctx, member, reason, f, users)    

async def purge(ctx, amount):
    log.com(ctx)
    try: amount = int(amount)+1 # Deletes initial command invoking command ### Adding a try catch doesn't work here idk why but if it's a non int it still passes
    except: await ctx.send("That's not a valid number"); return
    
    if amount <= 21 and amount > 0: await ctx.channel.purge(limit=amount); log.me(f"{amount-1} message(s) were cleared by the user")
    else: await ctx.send("Amount not supported"); log.me(f"Too many attempted message deletions! (Amount: {amount-1}") # Prevents an overzealous mod from deleting a channel
    
    del(ctx, amount)

async def mute(ctx, member):
    log.com(ctx)
    try: role = discord.utils.get(member.guild.roles, name="Muted"); await member.add_roles(role) # Attempts to get the servers muted role
    except discord.errors.Forbidden: await ctx.send("I can't assign that role! It's above my given role! Make sure my role is above Muted so I can assign this role!"); return
    except AttributeError: await ctx.send("You dont have a Muted role!\nPlease create a role named 'Muted' without quotes to make this function work"); return # If there is no muted role then it tells the end user that it could not find the muted role ### maybe make bot add Muted role?
    
    await ctx.send(f"{member} has been muted")
     
    try: await member.create_dm(); await member.dm_channel.send(f"Hi {member.name} you've been muted if you have any questions message the mods") # Attempts to DM a user
    except: await ctx.send("User's DM couldn't be reached") # If it cant then it lets the end user know that they cant be reached
     
    log.me(f"{member} was muted by user")

    del(ctx, member, role)

async def unmute(ctx, member):
    log.com(ctx)
    
    try: role = discord.utils.get(member.guild.roles, name="Muted"); await member.remove_roles(role) # Attempers to get the servers muted role 
    except discord.errors.Forbidden: await ctx.send("I can't unassign that role! It's above my given role! Make sure my role is above Muted so I can unassign this role!"); return
    except AttributeError: await ctx.send("You dont have a Muted role!\nPlease create a role named 'Muted' without quotes to make this function work"); return

    try: await member.create_dm(); await member.dm_channel.send(f"Hi {member.name} you've been unmuted") # Attempts to DM a user
    except: await ctx.send("User's DM couldn't be reached") # If it cant then it lets the end user know that they cant be reached
     
    log.me(f"{member} was unmuted by user")

    del(ctx, member, role)

async def ban(ctx, member, reason):
    log.com(ctx)
    
    try: 
        await member.ban(reason = reason)
        await ctx.send(f"{member} has been banned")
    except discord.errors.Forbidden: # This triggers if an admin tries to ban an owner or someone with higher permissions than the bot
        await ctx.send("This user can not be banned because they have a higher permission than the bot")
        log.me("User tried banning an admin")
        return
    
    # Attempts to DM a user
    try: await member.create_dm(); await member.dm_channel.send(f"Hi {member.name} you've been banned if you have any questions message the mods")
    except: await ctx.send("User's DM couldn't be reached") # If it cant then it lets the end user know that they cant be reached

    log.me(f"{member} was banned by user")
    
    del(ctx, member, reason)