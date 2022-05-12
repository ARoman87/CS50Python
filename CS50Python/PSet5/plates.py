def main():
    plate = input("Plate: ")
    print(is_valid(plate))


def is_valid(s):
    if len(s) <= 6 and len(s) >= 2 and s[:2].isalpha() and s.isalnum():
        if s[2].isdigit() and s[2] == "0":
            return False
        elif s[3].isdigit() and s[3] == "0" and len(s) > 4:
            return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    main()
