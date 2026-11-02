def main():
    bankgreet = value(input("Greeting: "))
    print(bankgreet)

def value(greeting):
    greet = greeting.lower().capitalize()
    if greet.startswith("Hello"):
        return "$0"
    elif greet[0] == "H":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()