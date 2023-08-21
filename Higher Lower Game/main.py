import random
import os
from game_data import data 
from art import logo, vs


def get_random_account(data):
    return random.choice(data)

def compare(account_a, account_b, guess):
  if account_a > account_b:
    return guess == "a"
  if account_b > account_a:
    return guess == "b"

def clear():
    os.system('cls||echo -e \\\\033c')

def game():
    print(logo)
    game_should_continue = True
    score = 0
    account_a = get_random_account(data)
    account_b = get_random_account(data)

    while game_should_continue:
        while account_a == account_b:
                account_b = get_random_account()

        print(f"score: {score}")
        print("Compare A: " + account_a["name"] + " a " + account_a["description"] + " from " +  account_a["country"])
        print(vs)
        print("Against B: " + account_b["name"] + " a " + account_b["description"] + " from " +  account_b["country"])

        guess = input("A or B: ").lower()
        if compare(account_a["follower_count"], account_b["follower_count"] ,guess):
            score += 1
            if guess == "b":
                account_a = account_b
            account_b = get_random_account(data)
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()