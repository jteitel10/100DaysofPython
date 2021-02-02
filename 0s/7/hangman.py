import random
import hangman_words
import hangman_art

stages = hangman_art.stages
end_of_game = False
lives = 6
chosen_word = random.choice(hangman_words.word_list)
display = ["_" for letter in chosen_word]

logo = hangman_art.logo
print(logo)

print(f"Chosen word: {chosen_word}")


while not end_of_game:
    guess = input("Guess a letter:\n").lower()
    if guess in display:
        print(f"You already guessed: {guess}\n")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])
