# Comment guide # = regular comment ## = section #/# = end of section ### = note to dev/self
### This file has been approved for a stable release as of revision 2

# Last Modified 7/24/2022

if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")

import random

async def randNum(ctx, difficulty):
    global num1
    global num2
    global randOper
    optList = ("+", "-", "*")
    if difficulty == "baby":
        num1 = random.randrange(0, 2)
        num2 = random.randrange(0, 2)
    elif difficulty == "easy":
        num1 = random.randrange(0, 10)
        num2 = random.randrange(0, 10)
    elif difficulty == "hard":
        num1 = random.randrange(0, 100)
        num2 = random.randrange(0, 100)
    elif difficulty == "nightmare":
        num1 = random.randrange(0, 1000)
        num2 = random.randrange(0, 100)
    elif difficulty == "hell":
        num1 = random.randrange(0, 1000)
        num2 = random.randrange(0, 1000)
    else:
        await ctx.send("Thats not a valid difficulty...\nDefaulting to hard")
        num1 = random.randrange(0, 100)
        num2 = random.randrange(0, 100)

    randOper = random.choice(optList)
    await ctx.send(f"QUICK! What is {num1}{randOper}{num2}?\nYou have 10 seconds to answer!")
    num1 = int(num1)
    num2 = int(num2)

def calc():
    global ans
    if randOper == "+": ans = num1 + num2
    elif randOper == "-": ans = num1 - num2
    elif randOper == "*": ans = num1 * num2

        
async def display(ctx, inp):
    global ans
    calc()
    try: inp = int(inp)
    except: await ctx.send("._. That isn't a number"); return
    if inp == ans: await ctx.send("Good job!")
    else: await ctx.send(f"Wrong! The answer was {ans}!")

async def timeoutAns(ctx):
    calc()
    await ctx.send(f"The answer was {ans}")

async def cleanup():
    global num1, num2, randOper, ans
    del(num1, num2, randOper, ans)