grocery_list = {}


while True:
    try:
        grocery_items = input("").upper()
        if grocery_items in grocery_list:
            grocery_list[grocery_items] += 1
        else:
            grocery_list[grocery_items] = 1
    except EOFError:
        for grocery_items in sorted(grocery_list):
            print(grocery_list[grocery_items], grocery_items)
        break
