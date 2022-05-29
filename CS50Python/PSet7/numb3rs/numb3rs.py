import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        num1, num2, num3, num4 = ip.split(".")
        num1, num2, num3, num4 = int(num1), int(num2), int(num3), int(num4)
        if num1 <= 255 and num2 <= 255 and num3 <= 255 and num4 <= 255:
            return True
        else:
            return False
    except ValueError:
        return False
