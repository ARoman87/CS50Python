import inflect

p = inflect.engine()

list = []
new_list = ""

while True:
    try:
        user_input = input("")
        list.append(user_input)
    except EOFError:
        new_list = p.join(list)
        print(f"Adieu, adieu, to {new_list}")
        break
