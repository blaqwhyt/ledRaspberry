import time
import random
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

name=raw_input("What is your name? ")
print "You are welcome, "+ name + "\n"
time.sleep(1)
print "Start guessing... \n \n \n "
time.sleep(0.5)

i=0
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
        
        while i < 5:
    
            GPIO.output(3, GPIO.HIGH)
            time.sleep(1.0)
            GPIO.output(3, GPIO.LOW)
            time.sleep(1)
            i=i+1
        
        print "You won \n"
        print "Thanks for playing \n"
        break
        
    guess = raw_input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns = turns - 1
        GPIO.output(5, True)
        time.sleep(1)
        GPIO.output(5, False)
        print "You have ", + turns, 'more guesses'

        if turns == 0:
           
            while i < 5:
    
                GPIO.output(5, GPIO.HIGH)
                time.sleep(1.0)
                GPIO.output(5, GPIO.LOW)
                time.sleep(1)
                i=i+1
            print "You loose"
    else:
        GPIO.output(3, True)
        time.sleep(1)
        GPIO.output(3, False)

GPIO.cleanup()
