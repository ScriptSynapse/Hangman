import tkinter as tk
from tkinter import messagebox
import random

# Word list
words = ["python", "hangman", "computer", "programming", "developer",
         "artificial", "intelligence", "challenge", "university", "notebook"]

# Difficulty settings
difficulty_levels = {
    "easy": 10,
    "medium": 7,
    "hard": 5
}


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game 🎯")
        self.root.geometry("500x700")

        self.word = ""
        self.guessed = []
        self.attempts = 0
        self.guessed_letters = []
        self.wins = 0
        self.losses = 0

        # Difficulty selector
        self.label = tk.Label(root, text="Choose Difficulty", font=("Arial", 16))
        self.label.pack(pady=10)

        self.difficulty_var = tk.StringVar(value="medium")
        for diff in difficulty_levels:
            tk.Radiobutton(root, text=diff.capitalize(),
                           variable=self.difficulty_var, value=diff).pack()

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        # Hangman canvas
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack(pady=20)

        # Game UI
        self.word_label = tk.Label(root, text="", font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.status_label = tk.Label(root, text="", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Wins: 0 | Losses: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.letter_frame = tk.Frame(root)
        self.letter_frame.pack(pady=20)

        # Bind keyboard events
        self.root.bind("<Key>", self.keyboard_input)

    def start_game(self):
        self.word = random.choice(words)
        self.guessed = ["_"] * len(self.word)
        self.guessed_letters = []
        self.attempts = difficulty_levels[self.difficulty_var.get()]
        self.update_display()
        self.create_letter_buttons()
        self.draw_hangman(0)

    def create_letter_buttons(self):
        for widget in self.letter_frame.winfo_children():
            widget.destroy()
        for c in "abcdefghijklmnopqrstuvwxyz":
            btn = tk.Button(self.letter_frame, text=c.upper(), width=4,
                            command=lambda letter=c: self.guess(letter))
            btn.grid(row=(ord(c) - 97) // 9, column=(ord(c) - 97) % 9)

    def keyboard_input(self, event):
        if event.char.isalpha():
            self.guess(event.char.lower())

    def guess(self, letter):
        if letter in self.guessed_letters:
            return
        self.guessed_letters.append(letter)

        if letter in self.word:
            for i, l in enumerate(self.word):
                if l == letter:
                    self.guessed[i] = letter
        else:
            self.attempts -= 1
            self.draw_hangman(difficulty_levels[self.difficulty_var.get()] - self.attempts)

        self.update_display()

        if "_" not in self.guessed:
            self.wins += 1
            messagebox.showinfo("🎉 You Won!", f"You guessed the word: {self.word}")
            self.start_game()
        elif self.attempts == 0:
            self.losses += 1
            messagebox.showinfo("💀 Game Over", f"You lost! The word was: {self.word}")
            self.start_game()

    def update_display(self):
        self.word_label.config(text=" ".join(self.guessed))
        self.status_label.config(text=f"Attempts left: {self.attempts}")
        self.score_label.config(text=f"Wins: {self.wins} | Losses: {self.losses}")

    def draw_hangman(self, step):
        """Draws hangman step by step"""
        self.canvas.delete("all")

        # Base stand
        self.canvas.create_line(50, 280, 250, 280, width=3)  # Base
        self.canvas.create_line(100, 280, 100, 50, width=3)  # Pole
        self.canvas.create_line(100, 50, 200, 50, width=3)   # Top bar
        self.canvas.create_line(200, 50, 200, 80, width=3)   # Rope

        # Draw body parts step by step
        if step >= 1:  # Head
            self.canvas.create_oval(175, 80, 225, 130, width=3)
        if step >= 2:  # Body
            self.canvas.create_line(200, 130, 200, 200, width=3)
        if step >= 3:  # Left arm
            self.canvas.create_line(200, 150, 170, 180, width=3)
        if step >= 4:  # Right arm
            self.canvas.create_line(200, 150, 230, 180, width=3)
        if step >= 5:  # Left leg
            self.canvas.create_line(200, 200, 170, 250, width=3)
        if step >= 6:  # Right leg
            self.canvas.create_line(200, 200, 230, 250, width=3)
        if step >= 7:  # Face (X eyes)
            self.canvas.create_line(185, 95, 195, 105, width=2)
            self.canvas.create_line(195, 95, 185, 105, width=2)
            self.canvas.create_line(205, 95, 215, 105, width=2)
            self.canvas.create_line(215, 95, 205, 105, width=2)


# Run the game
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
