# Higher_lower_project-
A simple command-line game built in Python where the player is shown two popular public figures (e.g., celebrities, brands, influencers) and must guess who has more followers on Instagram. The player keeps scoring as long as they guess correctly — one wrong guess ends the game!


# Game Logic Workflow
📦 Import Modules and Data

Random selection is handled using Python's random module.

The game uses preloaded data (data) from game_data.py.

ASCII art elements (logo, vs) are imported from art.py.

The terminal is cleared using a custom clear_screen() function that runs a shell command via os.

# Helper Functions

format_data(account): Formats an account’s name, description, and country into a printable string.

compare_account(f_account, s_account): Compares the follower counts of two accounts and returns the account ('A' or 'B') with more followers.

clear_screen(): Clears the terminal screen using:

python
Copy
Edit
os.system('cls' if os.name == 'nt' else 'clear')
# Game Setup

The game begins by printing the logo.

The initial score is set to 0.

A random account is selected as the first item to compare.

# Main Game Loop

The player is shown two accounts: A and B.

Account B is chosen to be different from account A.

The player inputs their guess: "A" or "B".

# Clear the Screen

The screen is cleared after each input using clear_screen() to keep the interface clean.

The logo is printed again for continuity.

# Evaluate Guess

If the player guesses correctly:

Score is incremented.

Account B becomes the new Account A.

If the guess is incorrect:

The game ends.

The final score is displayed.
