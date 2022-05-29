plate = input("Plate: ")
plate_list = []


def main():
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) == True and middle() == True:
        return True
    else:
        return False


def length(s):
    if len(s) <= 6 and len(s) >= 2 and s[:2].isalpha() and s.isalnum():
        return True
    else:
        return False


for i in plate:
    plate_list.append(i)


def middle():
    if plate_list[2].isdigit() and plate_list[2] == "0":
        return False
    elif plate_list[3].isdigit() and plate_list[3] == "0" and len(plate) > 4:
        return False
    else:
        return True


main()
