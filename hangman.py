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
words = ["python", "hangman", "computer", "programming", "developer",
         "artificial", "intelligence", "challenge", "university", "notebook"]

# Difficulty settings
difficulty_levels = {
    "easy": 10,
    "medium": 7,
    "hard": 5
}

print("🎯 Welcome to Hangman with Difficulty Levels!")
print("Choose a difficulty: Easy / Medium / Hard")

# Choose difficulty
while True:
    choice = input("Enter difficulty: ").lower()
    if choice in difficulty_levels:
        attempts = difficulty_levels[choice]
        break
    else:
        print("⚠️ Invalid choice! Please type: Easy, Medium, or Hard.")

# Pick a random word
word = random.choice(words)
guessed = ["_"] * len(word)
guessed_letters = []

print("\nGuess the word: ", " ".join(guessed))

# Game loop
while attempts > 0 and "_" in guessed:
    stage_index = min(len(stages) - 1, attempts)  # Prevent index errors
    print(stages[stage_index])
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

# Game result
if "_" not in guessed:
    print("\n🎉 You won! The word was:", word)
else:
    print(stages[0])
    print("\n💀 You lost! The word was:", word)
