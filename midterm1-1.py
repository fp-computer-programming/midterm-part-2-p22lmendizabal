# author: Lm (AMDG) 12/14/21
import random

def cloning(userinput):
    number = random.randint(0, 999)
    if number <= 999 or number >= 100:
        number = "0" + number
    elif number <= 99 or number >= 10:
        number = "00" + number
    else:
        number = "000" + number
    
    troopername = "CT-" + number
   
    
    while True:
        if userinput == "N" or userinput == "n":
                print(list(troopername))
                break
        elif userinput == "Y" or userinput == "y":
            continue
        else:
            

yesorno = input("Name a new clone? ")
