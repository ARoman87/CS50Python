def main():
    user_input = str(input("Write your word: "))
    print(shorten(user_input))


def shorten(word):
    vowels = "EIOUaeiou"
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word


if __name__ == "__main__":
    main()
