def main():
    user_input = input("Fraction: ")
    print(gauge(convert(user_input)))


def convert(fraction):
    x, y = fraction.split("/")
    if x.isdigit() and y.isdigit:
        x = int(x)
        y = int(y)
        percentage = (x / y) * 100
        return int(percentage)
    if y == 0:
        raise ZeroDivisionError
    else:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"
    ...


if __name__ == "__main__":
    main()
