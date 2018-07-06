import time
import random

name=raw_input("What is your name? ")
print "You are welcome, "+ name + "\n"
time.sleep(1)
print "Start guessing... \n \n \n "
time.sleep(0.5)

word="python"


guesses=''

turns=10

print "hint >> _ _t_ _n" 


while turns > 0:

    failed = 0
    for char in word:
        if char in guesses:
            print char,
        else:
            print "_",
            failed+=1

    if failed == 0:
        print "You won \n"
        print "Thanks for playing \n"
        break
        
    guess = raw_input("Guess a character: ")

    guesses += guess

    if guess not in word:
        turns = turns - 1
        print "Wrong Guess"
        print "You have ", + turns, 'more guesses'

        if turns == 0:
            print "You loose"
