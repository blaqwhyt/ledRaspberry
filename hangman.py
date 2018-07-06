import time
name=raw_input("What is your name? ")
print "You are welcome, "+ name
print ""
time.sleep(3)
print "Start guessing..."
time.sleep(0.5)

word="python"
print ""
print ""
print ""
print "hint >> _ _t_o_"

print ""
guesses=''

turns=10

while turns > 0:
failed = 0
for char in word:
if char in guesses
print char,
else:
print "_",
failed+=1
if failed == 0:
print "You won"
print ""
print "Thanks for playing"
break
print
guess = raw_input("Guess a character: ")

guesses += guess

if guess not in word:
turns -= 1
print "Wrong Guess"
print "You have " + turns, 'more guesses'

if turns == 0
print "You loose"