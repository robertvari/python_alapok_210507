import random

min_number = 1
max_number = 10

DEBUG = True

# Intro
print("="*50, "This is the Magic Number game.", "="*50)
print(f"You have to guess a number between {min_number}-{max_number}\n")

secret_number = str(random.randint(min_number, max_number))
if DEBUG:
    print(f"<<<DEBUG>>> secret_number: {secret_number}")

player_number = input("Your number?")


while player_number != secret_number:
    print("Wrong guess. Try again!")
    player_number = input("Your number?")

print("End of the game")