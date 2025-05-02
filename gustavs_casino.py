#!/usr/bin/env python3
# Created by: Gustav I
# Created on: April 28, 2025
# Description: Casino game with two mini-games – Slot Machine and Bomb Defusal

import random  # For random selection of symbols and codes
import time # For tracking the countdown timer
import codes  # Custom module containing possible bomb codes


# Function to get a valid game selection from the user
def get_valid_game_selection():
    while True:
        print("Welcome to Gustav's Casino. Select a game")
        print("Slot Machine (1) or Bomb Defusal (2)")
        selection = input("Enter your selection: ")
        # Check user input against valid choices
        if selection == "1" or selection.lower() == "slot machine":
            return 1
        elif selection == "2" or selection.lower() == "bomb defusal":
            return 2
        else:
            print("Invalid game selection. Please enter 1 or 2.")


# Function to get number of rounds the user wants to play
def get_number_of_plays():
    while True:
        try:
            plays = int(input("Enter the number of times you would like to play: "))
            if plays > 0:
                return plays
            else:
                print("Number of plays must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Function for the Slot Machine game
def slot_machine_spin():
    symbols = ["💎", "7", "🍒", "🍋", "🔔", "🍊", "🍉"]  # Slot machine symbols
    result = [random.choice(symbols) for _ in range(3)]  # Randomly select 3 symbols
    print("--------")
    print("Result")
    for symbol in result:
        print("|", symbol, "|", end="")  # Print slot result inline
    print()

    # Check for winning combinations
    if result == ["7", "7", "7"]:
        print("JACKPOT! YEEHAW")
    elif result == ["🍒", "🍒", "🍒"]:
        print("You got a small win!")
    elif result == ["💎", "💎", "💎"]:
        print("BLING BLING! YOU’RE THE REAL THING!")
    elif result == ["🔔", "🔔", "🔔"]:
        print("DING DING DING. WE GOT A WINNER!")
    else:
        print("Fun fact: 99 percent of gamblers quit before they win big.")


# Function for the Bomb Defusal game
def bomb_defusal_round():
    correct_code = random.choice(
        list(Codes.codes.keys())
    )  # Choose a random correct code
    print("Guess the code to defuse the bomb. You have 20 seconds")
    print("Available codes:")
    for code in Codes.codes.keys():
        print(code)

    start_time = time.time()  # Record the start time
    elapsed = 0

    # Continue while less than 20 seconds have passed
    while elapsed < 20:
        current_time = time.time()
        elapsed = int(current_time - start_time)
        print("Timer:", 20 - elapsed, "s remaining")
        user_code = input("Enter your code: ")

        # Check if code is correct and within time
        if user_code == correct_code and 0 <= elapsed < 20:
            print("Great you saved us all!")
            return
        else:
            print("Incorrect code. Try again!")

    # Time's up
    print("Call an ambulance! We’re hurt!")


# --- MAIN PROGRAM STARTS HERE ---
selection = get_valid_game_selection()  # Ask user to choose a game
plays = get_number_of_plays()  # Ask how many times they want to play
counter_plays = 0  # Track how many times they've played

# Repeat the selected game for the specified number of plays
while counter_plays < plays:
    if selection == 1:
        slot_machine_spin()  # Play slot machine
    elif selection == 2:
        bomb_defusal_round()  # Play bomb defusal
    counter_plays += 1  # Increment play counter
