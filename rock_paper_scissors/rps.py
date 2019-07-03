# Practicing all kind of stuff that I've learned over the past couple of 
# months. I'm sure that the game can be made much more simpler.

import random
import time

def intro():
    print("Welcome to Rock, Paper or Scissors!")
    x = input("Press enter to begin or R to read the rules!").lower()

    if x == "r":
        rules()

def rules():
    print("The rules are...")


def player_selection():
    while True:
        try:
            player_choice = int(input("Do you choose 1. Rock, 2. Paper or 3. Scissors? "))
            if 1 <= player_choice <= 3:
                if player_choice == 1:
                    print("You chose Rock!")
                    print("-" * 10)
                elif player_choice == 2:
                    print("You chose Paper!")
                    print("-" * 10)
                else:
                    print("You chose Scissors!")
                    print("-" * 10)
                break
            else:
                print("Please enter a number between 1-3.")
        except ValueError:
            print("Please enter a valid number between 1-3.")
    return player_choice


def computer_selection():
    computer_choice = random.randint(1, 3)
    print("Computer chooses.")
    time.sleep(1)
    print("Computer chooses..")
    time.sleep(1)
    print("Computer chooses...")
    time.sleep(1)

    if computer_choice == 1:
        print("Rock!")
        print("-" * 10)
    elif computer_choice == 2:
        print("Paper!")
        print("-" * 10)
    else:
        print("Scissors!")
        print("-" * 10) 

    return computer_choice


def battle(player_choice, computer_choice):
    print("Time to duel!")
    time.sleep(1)
    if player_choice == 1 and computer_choice == 1:
        print("Rock Vs. Rock ... It's a tie!")


if __name__ == "__main__":
    intro()
    player_points = 0
    computer_points = 0

    while player_points < 10 or computer_points < 10:
        player_choice = player_selection()
        computer_choice = computer_selection()
        battle(player_choice, computer_choice)