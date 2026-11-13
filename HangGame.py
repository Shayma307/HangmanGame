import random
# Hangman Game Function
def hangman(Easy, Medium, Hard):

    while True:

        print("\n========== HANGMAN GAME ==========")

        # Choose difficulty level
        level = input("Choose level (Easy / Medium / Hard): ").lower().strip()

        if level == "easy":
            words = Easy
        elif level == "medium":
            words = Medium
        elif level == "hard":
            words = Hard
        else:
            print("Invalid level! Try again.")
            continue

        # Choose a random fruit
        word = random.choice(words)

        # Number of chances = word length + 2
        chances = len(word) + 2
        guessed_letters = []
        guesses = 0

        print("\nGuess the fruit name!")
        print("Total chances:", chances)

        # Start guessing
        while guesses < chances:

            # Show hidden word
            hidden_word = ""

            for letter in word:
                if letter in guessed_letters:
                    hidden_word += letter + " "
                else:
                    hidden_word += "_ "

            print("\nWord:", hidden_word)
            print("Remaining chances:", chances - guesses)

            # Check if player won
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You WIN!")
                print("The word is:", word)
                break

            # Get player guess
            guess = input("Enter a letter: ").lower().strip()

            # Validate input
            if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter one English letter.")
                continue

            # Count every valid guess
            guesses += 1

            if guess in guessed_letters:
                print("You already guessed this letter!")

            else:
                guessed_letters.append(guess)

                if guess in word:
                    print("Correct!")
                else:
                    print("Wrong!")

        # Check final result
        if all(letter in guessed_letters for letter in word):
            print("\nYou guessed the fruit successfully!")
        else:
            print("\nGame Over! You LOST!")
            print("The correct word was:", word)

        # Ask to play again
        play_again = input("\nPlay again? (yes/no): ").lower().strip()

        if play_again != "yes":
            print("\nThanks for playing Hangman!")
            break


# Fruit lists
Easy = ["apple", "mango", "pear", "kiwi", "grape"]

Medium = ["banana", "orange", "papaya", "apricot", "coconut"]

Hard = ["pomegranate", "passionfruit", "blackcurrant",
        "persimmon", "mangosteen"]


# Run the game
hangman(Easy, Medium, Hard)
