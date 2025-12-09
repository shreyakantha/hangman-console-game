import random

words = ["RHYTHM", "EARTHQUAKE", "CHRISTMAS", "ZOMBIE", "SPAGHETTI"]

word = random.choice(words).upper()
guessed = set()
wrong_guesses = 0
max_wrong = 6
display = ["_"] * len(word)

hangman_stages = [
# Stage 0: No parts
    """
    +---+
    |   |
        |
        |
        |
        |
=========
""",
# Stage 1: Head
    """
    +---+
    |   |
    O   |
        |
        |
        |
=========
""",
# Stage 2: Head and body
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
=========
""",
# Stage 3: Head, body, left arm
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========
""",
# Stage 4: Head, body, both arms
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========
""",
# Stage 5: Head, body, both arms, left leg
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========
""",
# Stage 6:  Head, body, both arms, both legs
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========
"""
]

print("Welcome to Hangman!")
print("Guess the word one letter at a time. You have 6 wrong guesses.")

while wrong_guesses < max_wrong and "_" in display:
    print("\nCurrent word: " + " ".join(display))
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
    print("Hangman:")
    print(hangman_stages[wrong_guesses])
    
    guess = input("Guess a letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessed:
        print("You already guessed that letter.")
        continue
    
    guessed.add(guess)
    
    if guess in word:
        print("Good guess!")
        for i, letter in enumerate(word):
            if letter == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        wrong_guesses += 1

if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nSorry, you lost. The word was:", word)
    print("Final hangman:")
    print(hangman_stages[max_wrong])