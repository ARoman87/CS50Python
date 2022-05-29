greeting = str(input("Greeting: "))
greeting = greeting.casefold().strip()
greeting_h = greeting.startswith("h")

if "hello" in greeting:
    print("$0")
elif greeting_h:
    print("$20")
else:
    print("$100")
