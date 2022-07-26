# Last Modified 7/24/2022

if __name__ == "__main__": raise Exception("This is a module to the main bot.py file. This was not created to run independently")

async def RPS(ctx, option_set, gen, inp):
        if inp in option_set:
            await ctx.send(f"I choose {gen}, you chose {inp}!")
            
            if gen == inp: await ctx.send("You Tied!")
            elif inp == "rock" and gen == "paper": await ctx.send("You Lost!")
            elif inp == "paper" and gen == "scissors": await ctx.send("You Lost!")
            elif inp == "scissors" and gen == "rock": await ctx.send("You Lost!")
            else: await ctx.send("You Won!")
        
        else: await ctx.send("That doesn't work..")
        del(ctx, option_set, gen, inp)