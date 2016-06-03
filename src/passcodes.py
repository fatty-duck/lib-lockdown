#!/usr/bin/python
import ConfigParser as cp

# Module named configparser in Python 3; ConfigParser in Python 2


config = cp.RawConfigParser()
config.read("..\passcodes.cfg")

passcodes= config.get("Main","passcodes").lower().split(",")
old_passcodes= []

total = len(passcodes)

if config.get("Main", "bronze"):
    bronze = int(config.get("Main", "bronze"))
else:
    bronze = total
    
if config.get("Main","silver"):
    silver = int(config.get("Main","silver"))
else:
    silver = total
gold = total
count = 0

# check len of passcodes is more than silver & silver more than bronze


intro_text = config.get("Text","intro")
prompt_text = config.get("Text","prompt")
bronze_text = config.get("Text","bronze")
silver_text = config.get("Text","silver")
gold_text = config.get("Text","gold")

ascii_correct = config.get("ASCII","correct")
ascii_welcome = config.get("ASCII","welcome")
ascii_incorrect = config.get("ASCII","incorrect")
ascii_oops = config.get("ASCII","previous_guess")
ascii_gold = config.get("ASCII","gold")
ascii_bronze = config.get("ASCII","bronze")
ascii_silver = config.get("ASCII", "silver")


def passcode_check(guess):
    if guess in passcodes:
        passcodes.remove(guess)
        old_passcodes.append(guess)
        
        global count
        count += 1
        
        # ASCII art "correct"
        print ascii_correct 
           
        
        print str(count), " of ", str(total), " puzzles solved.\n"

    elif guess in old_passcodes:
        # ASCII art "oops!"
        print ascii_oops
        print "\nPasscode already recorded"
    else:
        # ASCII art "Incorrect"
        print ascii_incorrect
        print "\nPASSCODE DOES NOT MATCH"    


if total < silver or silver < bronze:
    print "Total number of passcodes cannot be less than silver, silver cannot be less than bronze. Please review number of passcodes and values for silver and bronze:\n"
    print "Number of passcodes:\t" + str(total)
    print "Silver:\t\t\t" + str(silver)
    print "Bronze:\t\t\t" + str(bronze)
    raw_input("Press Enter to exit program...")
    exit()
        
        
# Intro ASCII art "Welcome"
print ascii_welcome

# Introduction/explanatory text
print intro_text


while count < bronze:
    guess = raw_input(prompt_text).lower()
    passcode_check(guess)
        

print ascii_bronze

        
print bronze_text

while count < silver:
    guess = raw_input(prompt_text).lower()
    passcode_check(guess)

print ascii_silver
print silver_text    
    
while count < gold:
    guess = raw_input(prompt_text).lower()
    passcode_check(guess)


print ascii_gold
raw_input(gold_text)