from art import logo, vs
from data import data
import random
import os


def clear_console():
    os.system('cls')


def format_data(account):
    """Format the account data into printable format."""
    account_name = account['name']
    account_des = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_des}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Use if statement to check if the user is correct"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


score = 0
print(logo)
account_a = random.choice(data)
game_on = False
while not game_on:
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear_console()

    if is_correct:
        score += 1
        print(f"You are right, Current score {score}")
        account_a = account_b

    else:
        print(f"Sorry, thats wrong. Final score {score}")
        game_on = True
