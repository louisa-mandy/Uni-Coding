#create a random number guessing game using the library random, but the user
#has limited amount of tries (hint use while loops)

import random
import math
# Taking lower Inputs
lower = int(input("Enter Lower bound:- "))

# Taking upper Inputs
upper = int(input("Enter Upper bound:- "))

# generating random number between the lower and upper number 

x = random.randint(lower, upper) # randint - random integer 
print("\n\tYou only have ", 
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("yeyy Congratulations you did it in ",
			count, " tries")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too little!")
	elif x < guess:
		print("bestie, You Guessed too high! -_-")

# if over maximum guesses, then do this

if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tbe better bro!")
 
# Better to use This source Code on pycharm!
