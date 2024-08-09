word_list = ["apple", "cherry", "grape", "orange", "pear", "pineapple"]
import random
chosen_word = random.choice(word_list)
guessed_letters = []  # To store guessed letters
attempts = 7         # Number of allowed incorrect guesses

while attempts > 0:
    # Display the current state of the word (with underscores for unguessed letters)
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in chosen_word])
    print(f"Word: {display_word}")

    # Ask the player for a guess
    guess = input("Guess a letter: ").lower()
            
    # Check if the guess is valid (a single letter) and not already guessed
    if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
        guessed_letters.append(guess)
        if guess not in chosen_word:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word. You have {attempts} attempts left.")
        else:
            print(f"Great guess! '{guess}' is in the word.")
    else:
        print("Invalid input. Please enter a single letter you haven't guessed before.")

    # Check if the player has won
    if "_" not in display_word:
        print(f"Congratulations! You guessed the word: {chosen_word}")
        break

if attempts == 0:
    print(f"Sorry, you're out of attempts. The word was: {chosen_word}")
