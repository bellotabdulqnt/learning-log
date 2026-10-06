greet = input("Greeting: ").lower().capitalize()
if greet.startswith("Hello") == True:
    print("$0")
elif greet[0] == "H":
    print("$20")
else:
    print("$100")
