user_input = str(input("Write a text: "))


def kill_vowels(user_input):
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        user_input = user_input.replace(vowel, "")
    print(f"Output: {user_input}")


print(f"Input: {user_input}")
kill_vowels(user_input)
