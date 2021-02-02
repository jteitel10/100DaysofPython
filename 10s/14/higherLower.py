from art import logo, vs
from gameData import data
import random
# function to check follower counts
def check_counts(A, B, guess):
    if A > B:
        return guess == "a"
    else:
        return guess == "b"
# function to select a random data
def select_rand_user():
    return random.choice(data)
# play game function
def play_game():
    print(logo)
    score = 0
    # randomly select starting two accounts to compare
    compare_A = select_rand_user()
    compare_B = select_rand_user()
    # while loop flag
    should_continue = True
    # while loop
    while should_continue:
        compare_A = compare_B
        compare_B = select_rand_user()
        while compare_A == compare_B:
            compare_B = select_rand_user()
        print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}.\n" + vs + f"\nCompare B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}.\n")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        # format the follower counts for checking
        a_count = compare_A['follower_count']
        b_count = compare_B['follower_count']
        # check the guess
        is_correct = check_counts(a_count, b_count, guess)
        # if correct, increase score and play again. if wrong, end game.
        if is_correct:
            score += 1
            print(f"Correct! {compare_A['name']} has more followers. Your score is {score}.\n")
        else:
            print(f"Incorrect. {compare_B['name']} has more followers.  Game over.  Your score is {score}.\n")
            should_continue = False
play_game()
