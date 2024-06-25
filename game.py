import random

COLORS = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE'] # 6 colors
TRIES = 10
CODE_LENGTH = 4

# generate random code
def generate_code():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)] #generate 4 random colors

# guess the code
def guess_code():
    while True:
        guess = input("Enter your guess (separate colors by space): ").upper().split(" ") #convert to uppercase and split by space
#check if the guess is of the correct length
        if len(guess) != CODE_LENGTH:
            print(f"Your guess must be {CODE_LENGTH} colors.")
            continue
#check if the guess is of the correct color
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Please try again.")
                break
        else:
            break
    return guess

# check the guess
def check_guess(real_code, guess):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

#count the colors in the code
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    # First pass: count correct positions
    for i in range(CODE_LENGTH):
        if guess[i] == real_code[i]:
            correct_pos += 1
            color_counts[real_code[i]] -= 1

    # Second pass: count incorrect positions
    for i in range(CODE_LENGTH):
        if guess[i] != real_code[i] and guess[i] in color_counts and color_counts[guess[i]] > 0:
            incorrect_pos += 1
            color_counts[guess[i]] -= 1

    return correct_pos, incorrect_pos

# play the game
def play_game():
    print("Welcome to Mastermind!")
    print(f"You have {TRIES} attempts to guess the code.")
    print("The possible colors are:", COLORS)
    print("A color may appear more than once in the code.\n")

    code = generate_code()
    # Uncomment the next line to see the code for testing purposes
    # print(f"Secret code for testing: {code}")

    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_guess(code, guess)

        if correct_pos == CODE_LENGTH:
            print(f"Congratulations! You guessed the code in {attempt} attempts.")
            break

        print(f"Attempt {attempt}: {correct_pos} correct position(s), {incorrect_pos} incorrect position(s).")

    else:
        print(f"Sorry! You did not guess the code in {TRIES} attempts. The code was {code}.")

if __name__ == "__main__":
    play_game()
