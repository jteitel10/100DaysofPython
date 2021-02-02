import random

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def num_check(comp_num, user_num, lives):
    if comp_num == user_num:
        print ("You guessed the right number! You Win!")
    elif comp_num > user_num:
        print("Too Low!")
        return lives - 1
    else:
        print ("Too High!")
        return lives - 1

def set_difficulty():
    difficulty = input("I'm thinking of a number between 1 and 100.\nChoose a difficulty.  Type 'easy' or 'hard'\n").lower()
    if difficulty == 'easy':
        return EASY_LEVEL_LIVES
    else:
        return HARD_LEVEL_LIVES

def play_game():
    print("Welcome to the Number Guessing Game!")
    user_lives = set_difficulty()
    computer_guess = random.randint(1,100)
    user_guess = 0
    while user_guess != computer_guess:
        user_guess = int(input("Make a guess:\n"))
        user_lives = num_check(computer_guess, user_guess, user_lives)
        if user_lives == 0:
            print ("Your run out of guesses, you lose.")
            return
        elif user_guess != computer_guess:
            print("Guess Again!")

play_game()
