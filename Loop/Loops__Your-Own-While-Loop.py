from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)


# Start your game!
def main():
	guesses_left = 3 #Look at this as lifecount
	while guesses_left > 0:
	    #guess = int(raw_input("Your guess: "))
	    guess = int(raw_input('Guess a number (1-10):'))
	    if guess == random_number:
	        print 'You win!'
	        break
	    guesses_left -= 1
	        #guess = random_number
	else:
	    print 'You lose.'   
print main()