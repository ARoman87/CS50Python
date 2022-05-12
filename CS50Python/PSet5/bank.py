
def main():
    greeting = str(input("Greeting: "))
    print(value(greeting))


def value(greeting):
    greeting = greeting.casefold().strip()
    greeting_h = greeting.startswith("a")  # this is where the mistake is at
    if "hello" in greeting:
        return 0
    elif greeting_h:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
