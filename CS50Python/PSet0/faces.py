def convert(faces):
    faces = faces.replace(":)", "🙂").replace(":(", "🙁")
    print(faces)


def main():
    user_input = input()
    convert(user_input)


main()
