
coke_price = 50


while coke_price > 0:
    print(f"Amount Due: {coke_price}")
    user_input = int(input("Insert Coin: "))

    if user_input == 25 or user_input == 10 or user_input == 5:
        coke_price = coke_price - user_input
else:
    print(f"Change owed: {abs(coke_price)}")
