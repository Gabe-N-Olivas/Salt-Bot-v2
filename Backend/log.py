### This file has been approved for a stable release as of revision 2
# Last Modified 7/24/2022

if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")

try: from datetime import datetime
except ImportError: raise ImportError("Import error in log.py: One or more imports are missing!\nList of imports used: 'datetime'\nTry updating or installing these with pip")

def me(logInfo):
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    logMe = open(f"../log.me", "a", encoding="utf8")
    print(f"{time} {logInfo}", file=logMe), logMe.close()

def com(ctx):
    me(f"{ctx.message.author} used the command \"{ctx.command}\"")