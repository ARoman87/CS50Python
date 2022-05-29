import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    print(s)
    word = re.findall("\\bum\\b", s)
    return len(word)


...


if __name__ == "__main__":
    main()
