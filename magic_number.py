import random

# constants
min_number = 1
max_number = 10
max_tries = 3

DEBUG = True

# Intro
print("="*50, "This is the Magic Number game.", "="*50)
print(f"You have to guess a number between {min_number}-{max_number}\n")

secret_number = str(random.randint(min_number, max_number))
if DEBUG:
    print(f"<<<DEBUG>>> secret_number: {secret_number}")

player_number = input("Your number?")


while player_number != secret_number:
    max_tries -= 1
    if max_tries == 0:
        print("You died!")
        break

    print("Wrong guess.")
    print(f"You have {max_tries} lives left.")
    print("Try again.")
    player_number = input("Your number?")

if player_number == secret_number:
    print(f"You win! My number was: {secret_number}")
else:
    print("You lost the game :( Maybe next time!")