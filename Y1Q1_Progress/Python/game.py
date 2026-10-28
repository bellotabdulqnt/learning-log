import random as rnm
def main():
    while True:
        try:
            guesser(int(input("Level: ")))
            break
        except ValueError:
            pass
    

def guesser(n):
    guessee = rnm.randint(1, n)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                pass
            elif guess < guessee:
                print("Too small!")
            elif guess > guessee:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass
main()