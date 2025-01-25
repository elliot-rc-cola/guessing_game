# number guessing game
# generate random number between 1 and 100
# user has to guess the number in five attemps
# if the guesss is too high or too low, the program prints 'too high' or 'too low'
# if the user guesses within five digits of the number, the program prints 'getting close!'
# if the user guesses correctly, the program prints 'you win!'
# if the user doesn't guess correctly, the program prints 'sorry, the number was <number>'
# win or lose, the program prints 'do you want to play again? (y/n)'
# eithe game will either reset or end depending on user input

# import random library
import random 

#list of encouraging words for the guess promts rather than repeating 'Give me your best guess...'
encouragement = ["Don't give up... ", "You can do it... ", "You'll get it this time... ", "Guess again... ", "Dig deep... ", "You can do better than that... "]

# let's get into it
def guessing_game():
    # variable to store random number
    number = random.randint(1,100) 

    # variable to count number of attempts
    attempts = 0

    # welcome message and rules
    print('Welcome to the guessing game!')
    print("I'm thinking of a number between 1 and 100...")
    print("You'll have five attempts to guess the number.")
    print("After each guess I'll give you a hint and let you know how many attempts you have left.")
    print('Good luck!')

    #user enters first guess to being the game loop
    guess = input("Give me your best guess... ")

    # ah yes, how could we forget error handling?! 
    # ensuring the guesses are numbers less than 100 but greater than 0.
    if guess.isalnum() == True:
        print('Please use numbers 0-9 for this game.')
        guess = input("Give me your best guess... ")
    if guess.isalpha() == True:
        print('Please use numbers 0-9 for this game.')
        guess = input("Give me your best guess... ")
    if guess.isdigit() == False:
        print('Please use numbers 0-9 for this game.')
        guess = input("Give me your best guess... ")
    elif int(guess) <= 0:
        print('Clever, but stick to numbers between 1 and 100.')
        guess = input("Give me your best guess... ")
    elif int(guess) >= 101:
        print('Woah there! This game only goes up to 100.')
        guess = input("Give me your best guess... ")

    # use a while loop to keep the game active, so long as the user has attempts left. 
    # conditionals to guide the game based on the closeness of the guesses
    while attempts <= 4:
        print(number)
        if int(guess) > number and  int(guess) <= number + 10:
            attempts += 1
            print('Getting close but too high!')
        elif int(guess) > number:
            attempts += 1
            print('Too high!')
        elif int(guess) < number and int(guess) >= number - 10:
            attempts += 1
            print('Getting close but too low!')
        elif int(guess) < number:
            attempts += 1
            print('Too low!')
        elif int(guess) == number:
            print("You win!")
            play_again = input('Do you want to play again? (y/n) ')

            # error handling for play_again, anything other than 'y' or 'n' is handled by this error
            if play_again.lower() not in ['y', 'n']:
                print("Please type 'y' for yes and 'n' for no.")
                play_again = input('Do you want to play again? (y/n) ')

            # restarting or ending the game
            if play_again.lower() == 'y':
                attempts = 0
                guessing_game()
            elif play_again.lower() == 'n':
                print('Thanks for playing!')

        # to count the number of attempts and change the message on the final attempt
        if attempts <= 4:
            print('You have ' + str(5 - attempts) + ' attemps left.')
            guess = input(random.choice(encouragement))
        else: 
            print('Last chance!')
            guess = input("Give me your best guess... ")

    # when the user has run out of guesses
    if attempts == 5:
        print(f'Sorry, the number was {number}')
        play_again = input('Do you want to play again? (y/n) ')
            

guessing_game()