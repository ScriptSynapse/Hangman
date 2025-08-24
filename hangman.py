import random

# Hangman ASCII stages
stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    
       |    
       |    
       |
    =========
    """
]

# Word list
words = ["python", "hangman", "computer", "programming", "developer", "artificial", "intelligence"]

# Pick a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = len(stages) - 1
guessed_letters = []

print("🎯 Welcome to Hangman with ASCII Art!")
print("Guess the word: ", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    print(stages[attempts])  # Show current hangman state
    guess = input("\nEnter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f"✅ Nice! '{guess}' is in the word.")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"❌ '{guess}' is not in the word. Attempts left: {attempts}")

    print(" ".join(guessed))

# Game over
if "_" not in guessed:
    print("\n🎉 You won! The word was:", word)
else:
    print(stages[0])  # Final hangman
    print("\n💀 You lost! The word was:", word)
