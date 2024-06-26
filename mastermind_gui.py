import random
import tkinter as tk
from tkinter import messagebox

# Constants
COLORS = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE'] 
TRIES = 10
CODE_LENGTH = 4

# Functions
def generate_code(): # Generates a random code
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)] # Returns a list of 4 random colors

# Main class
class MastermindGame: 
    def __init__(self, root): # Constructor 
        self.root = root # Tkinter root window
        self.root.title("Mastermind Game") # Title of the window
        
        self.code = generate_code() # Generates a random code
        self.attempts = 0 # Number of attempts
        
        self.create_widgets() # Creates the widgets
        
    def create_widgets(self): # Creates the widgets
        self.label = tk.Label(self.root, text="Welcome to Mastermind! Guess the code:") # Label
        self.label.pack(pady=10)
        
        self.color_vars = [tk.StringVar(value="") for _ in range(CODE_LENGTH)] # String variables
        self.color_entries = [tk.Entry(self.root, textvariable=self.color_vars[i]) for i in range(CODE_LENGTH)] # Entry widgets
        
        for entry in self.color_entries: # For each entry widget
            entry.pack(side=tk.LEFT, padx=5) # Packs the entry widget
        
        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.check_guess) # Button
        self.submit_button.pack(pady=20)
        
        self.result_label = tk.Label(self.root, text="") # Label
        self.result_label.pack(pady=10) # Packs the label
        
    def check_guess(self): # Checks the guess
        guess = [var.get().upper() for var in self.color_vars] # Gets the guess
        
        if len(guess) != CODE_LENGTH or any(color not in COLORS for color in guess): # If the guess is invalid
            messagebox.showerror("Error", f"Your guess must be {CODE_LENGTH} colors from {COLORS}") # Shows an error message
            return
        
        correct_pos, incorrect_pos = self.calculate_feedback(self.code, guess) # Calculates the feedback
        
        self.attempts += 1
        result_text = f"Attempt {self.attempts}: {correct_pos} correct positions, {incorrect_pos} incorrect positions" # Result text
        self.result_label.config(text=result_text) # Configures the result label
        
        if correct_pos == CODE_LENGTH: # If the guess is correct
            messagebox.showinfo("Congratulations!", f"You guessed the code in {self.attempts} attempts!")  # Shows a message
            self.reset_game()
        elif self.attempts >= TRIES: # If the player has no more attempts
            messagebox.showinfo("Game Over", f"You did not guess the code in {TRIES} attempts. The code was {self.code}.") # Shows a message
            self.reset_game()
    
    def calculate_feedback(self, real_code, guess): # Calculates the feedback
        color_counts = {} 
        correct_pos = 0
        incorrect_pos = 0
        
        for color in real_code: # For each color in the real code
            if color not in color_counts: # If the color is not in the color counts
                color_counts[color] = 0 # Adds the color to the color counts
            color_counts[color] += 1
        
        for i in range(CODE_LENGTH): # For each index in the code
            if guess[i] == real_code[i]: # If the guess is correct
                correct_pos += 1
                color_counts[real_code[i]] -= 1
        
        for i in range(CODE_LENGTH): # For each index in the code
            if guess[i] != real_code[i] and guess[i] in color_counts and color_counts[guess[i]] > 0: # If the guess is incorrect but the color is in the color counts
                incorrect_pos += 1 # Increments the incorrect position
                color_counts[guess[i]] -= 1 # Decrements the color count
        
        return correct_pos, incorrect_pos # Returns the correct and incorrect positions
    
    def reset_game(self): # Resets the game
        self.code = generate_code() # Generates a new code
        self.attempts = 0 # Resets the number of attempts
        self.result_label.config(text="") # Configures the result label
        for var in self.color_vars: # For each color variable
            var.set("") # Sets the color variable to an empty string

# Main code 
if __name__ == "__main__": # If the script is executed
    root = tk.Tk() # Creates a Tkinter root window
    game = MastermindGame(root) # Creates a Mastermind game
    root.mainloop() # Runs the Tkinter main event loop
