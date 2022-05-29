import random
import sys

while True:
    level = input("Level: ")
    try:
        if level.isdigit():
            level = int(level)
            if level > 0:
                break
    except ValueError:
        continue

num1 = random.randint(1, level)

while True:
    guess = input("Guess: ")
    try:
        if guess.isdigit():
            guess = int(guess)
            if guess > 0:
                if guess > num1:
                    print("Too large!")
                elif guess < num1:
                    print("Too small!")
                elif guess == num1:
                    sys.exit("Just right!")
    except EOFError:
        break
