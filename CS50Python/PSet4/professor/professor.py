import random
import sys


def main():
    score = 0
    tries = 1
    wrong_answers = 0
    level = get_level()

    while tries <= 10:
        x = generate_interger(level)
        y = generate_interger(level)

        while tries <= 10:
            user_input = input(f"{x} + {y} = ")
            if user_input.isdigit():
                user_input = int(user_input)
                if user_input == x + y:
                    tries += 1
                    score += 1
                    break
            if user_input != x + y:
                print("EEE")
                tries += 1
                wrong_answers += 1
                if wrong_answers == 3:
                    print(f"{x} + {y}: ", x + y)
                    wrong_answers = 0
                    break
                else:
                    continue

    print("Score: ", score)


def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit():
            level = int(level)
            if level <= 3 and level >= 1:
                return level


def generate_interger(level):
    if level == 1:
        level = random.randint(0, 9)
    elif level == 2:
        level = random.randint(10, 99)
    elif level == 3:
        level = random.randint(100, 999)
    return level


if __name__ == "__main__":
    main()
