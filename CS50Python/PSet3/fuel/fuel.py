while True:
    try:
        user_input = input("Fraction: ")
        user_input = user_input.split("/")
        x = int(user_input[0])
        y = int(user_input[1])
        percent = (x / y) * 100
        if percent > 100:
            continue
    except (ValueError, ZeroDivisionError):
        continue
    else:
        break

if percent < 1:
    print("E")
elif percent > 99:
    print("F")
else:
    print(f"{percent:.0f}%")
