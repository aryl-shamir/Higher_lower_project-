from game_data import data
from art import logo, vs
import random
import os


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def format_data(account):
    """A function that takes an account as input then  return his name description and country as format"""

    name = account['name']
    description= account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def compare_account(f_account, s_account):
    """A function that compare the followers account, and return the account with the highest follower account"""
    a_followers = f_account["follower_count"]
    b_followers = s_account["follower_count"]

    if a_followers > b_followers:
        return "A"
    else:
        return "B"


first_account = random.choice(data)
print(logo)
score = 0
game_over = False

while not game_over:

    print(f"Compare A: {format_data(first_account)}")
    print(vs)

    second_account = random.choice(data)
    while second_account == first_account:
        second_account = random.choice(data)

    print(f"Against B: {format_data(second_account)}")
    correct_answer = compare_account(first_account, second_account)
    guest = input("Who has more followers? Type 'A' or 'B': ").upper()

    #clear the screen
    clear_screen()
    print(logo)
    # If user uses invalid input like c and d
    if guest not in ["A", "B"]:
        print("Invalid input, please type 'A' or 'B' ")
        continue

    if guest == correct_answer:
        score += 1
        first_account = second_account
        print(f"You're right. Current score: {score}")
    else:
        game_over = True
        print(f"Sorry that's wrong. Final score: {score}")
