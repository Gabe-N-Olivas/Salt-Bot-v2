### This file has been approved for a stable release as of revision 2

if __name__ != "__name__": raise Exception("This script was not created to be run as a module") 

from passlib.hash import bcrypt

password= input("Enter a password > ")
hashed = bcrypt.hash(password)
logMe = open(f"./Backend/hash", "a", encoding="utf8")
print(f"{hashed}", file=logMe), logMe.close()
print(hashed)
print("Hash saved to ./Backend/hash\nPlease clear your terminal")