deep_answer = str(input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "))

deep_answer = deep_answer.casefold().strip()

if deep_answer == "42" or deep_answer == "forty-two" or deep_answer == "forty two":
    print("Yes")
else:
    print("No")
