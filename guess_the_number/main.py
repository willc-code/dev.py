import random

print("Welcome to the Number Guessing Game! Please enter a number between 1 and 9 to make your guess.\n")
game_over = False
attempts = 0

while game_over == False:
    secret_number = random.randint(1, 9)
    guess = int(input("what's your guess? "))
    if guess == secret_number:
        attempts += 1
        print(f"The number was {secret_number}")
        print(f"You got it!")
        if attempts <= 2:
            print("I bet you could read minds!")
        elif attempts <= 5:
            print("Not bad!")
        else:
            print("I admire your perseverence!")
        game_over = True
    if guess != secret_number:
        attempts += 1
        print(f"The number was {secret_number}")
        print("Try again!")
        game_over = False