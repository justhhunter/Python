#Hunter Copening
# 6/6/2022

# Lab Guess the Number

# This program will choose a random number from 1 to 1000. It will then take user input as a "guess"
# The program will keep track of the number of guesses and whether the number is guessed correctly.



# import random module
import random




# main module

def main():
    # initialize variables
    playagain = 'yes'
    
    userguess = 0 

    # create random number generator
    randomnumber = random.randint(1, 1000)
        
    

    # keeps track of number of guesses
    guesscounter = 0

    # while loop to start program

    while playagain == 'yes':

        # prompt user for guess input
        userguess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))
        

        # if user guesses too high
        if userguess > randomnumber:
            print('Too high. Try again.')

            

        # if user guesses too low
        elif userguess < randomnumber:
            print('Too low. Try again.')

            

        elif userguess == randomnumber:

            print('Congratulations. You guessed the number!')

            

            if guesscounter <= 10:

                print('Either you know the secret or you got lucky!')

            elif guesscounter > 10:

                
                print('You should be able to do better!')

            playagain = input('Would you like to play again (yes/no): ')

        guesscounter += 1

main()