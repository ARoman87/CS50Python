from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 3 or len(sys.argv) == 2:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            user_input = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(user_input))
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")


else:
    user_input = input("Input: ")
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    print(figlet.renderText(user_input))
