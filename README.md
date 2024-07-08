# Mastermind Game

Mastermind is a classic code-breaking game where the player tries to guess a secret code consisting of a series of colors. This version of the game is implemented in Python using the `tkinter` library to provide a graphical user interface (GUI).

## Features

- **Random Code Generation**: The secret code is randomly generated each game, ensuring a unique challenge every time.
- **Graphical User Interface**: The game features an intuitive GUI built with `tkinter`.
- **Feedback Mechanism**: After each guess, the player receives feedback on the number of correct colors in the correct positions and correct colors in incorrect positions.
- **Multiple Attempts**: The player has a limited number of attempts to guess the code.

## How to Play

1. Run the game by executing the Python script.
2. Enter your guess by typing the colors in the provided entry fields.
3. Click the "Submit Guess" button to see the feedback.
4. Continue guessing until you either guess the code correctly or run out of attempts.
5. A message will display your success or the correct code if you fail to guess it within the allowed attempts.

## Installation

To run the Mastermind game, you need to have Python installed. Follow these steps:

1. Clone the repository:
    
2. Navigate to the project directory:
    ```sh
    cd mastermind-game
    ```
3. Install the required dependencies. For this project, `tkinter` is used, which is included with standard Python installations.

4. Run the game:
    ```sh
    python mastermind_gui.py
    ```

## Game Screenshot

![

## Code Overview

### Main Components

- `generate_code()`: Generates a random code consisting of 4 colors.
- `MastermindGame` Class:
  - `__init__(self, root)`: Initializes the game, sets up the GUI, and generates a new code.
  - `create_widgets(self)`: Creates and arranges the GUI elements.
  - `check_guess(self)`: Validates the user’s guess and provides feedback.
  - `calculate_feedback(self, real_code, guess)`: Calculates the number of correct and incorrect positions in the guess.
  - `reset_game(self)`: Resets the game state for a new game.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

Enjoy playing Mastermind!
