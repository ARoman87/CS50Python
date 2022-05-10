name = input("What is you name? ")


def case_change(name):
    case = [name[0].lower()]
    for c in name[1:]:
        if c in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            case.append("_")
            case.append(c.lower())
        else:
            case.append(c)

    return "".join(case)


print(case_change(name))
