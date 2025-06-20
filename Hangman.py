import random

words = ["apple", "table", "chair", "house", "plant"]
max_incorrect = 6

def display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])

def hangman():
    print("Welcome to Hangman!")
    while True:
        word = random.choice(words)
        guessed = set()
        incorrect = 0
        print(f"\nNew word to guess! ({len(word)} letters)")
        while incorrect < max_incorrect:
            print(f"Word: {display_word(word, guessed)}")
            print(f"Incorrect guesses left: {max_incorrect - incorrect}")
            guess = input("Guess a letter: ").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter.")
                continue

            if guess in guessed:
                print("You already guessed that letter.")
                continue

            guessed.add(guess)
            if guess in word:
                print("Correct!")
                if all(letter in guessed for letter in word):
                    print(f"Congratulations! You guessed the word: {word}")
                    break
            else:
                print("Incorrect!")
                incorrect += 1
        else:
            print(f"Game over! The word was: {word}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    hangman()