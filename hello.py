from datetime import datetime
from time import sleep
from random import randint

current_daytime = datetime.now()
print("Hello, World! and welcome to Daniel Morrisey's Python Playground")
print("Python Projects I made to learn and for fun!")
print("Today's is " + str(current_daytime.month) + "/" + str(current_daytime.day) + "/" + str(current_daytime.year) + ",")
print("")
print("Now that I have told you about me, I want to learn about you!")
print("Your data is stored locally and not shared with anyone.")
first_name = input("What is your first name? ")
print("Hello " + first_name + ", nice to meet you!")
print("")
import os

def run_about():
    user_input = input("Do you want to learn more about me? (type yes or no)").strip().lower()
    if user_input == "yes":
        os.system("python about.py")  # Runs the about.py file
    elif user_input == "no":
        print("Skipping execution.")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

run_about()
print("")
print("Let's play a game, " + first_name + "!")
print("It's time to roll the dice three times and see which number is the highest! Are you ready?")

input("Press Enter to roll the dice...")

rolls = []
for i in range(1, 4):
    roll = randint(1, 6)
    print(f"Roll {i}: {roll}")
    rolls.append(roll)
    sleep(1)

highest = max(rolls)
print(f"\nThe highest number you rolled is: {highest}!")

print("Thanks for playing, " + first_name +"!")

input("Let's play another game?")
print("Great! Let's play again!")
print("")
print("This time, let's play a guessing game.")
print("I will think of a number between 1 and 100, and you have to guess it!")
print("You have 13 tries to guess the number.")
print("Are you ready? Let's go!")
input("Press Enter to start the game...")
number_to_guess = randint(1, 100)
tries = 13
while tries > 0:
    guess = int(input(f"You have {tries} tries left. What's your guess? "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("")
        print("Congratulations! You guessed the number!")
        break
    tries -= 1
if tries == 0:
    print(f"Sorry, you've run out of tries. The number was {number_to_guess}.")
print("Thanks for playing the guessing game, " + first_name + "!")
print("I hope you had fun!")
print("")
print("_________________________")
print("Follow me on Bluesky @madebydanny.uk")
print("Fork this project on GitHub! @ therealfuntimeswithdanny/python-playground")
print("_________________________")
print("End of Python Script")
print("Code is open source and free to use!")