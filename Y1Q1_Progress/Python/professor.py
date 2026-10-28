import random

def main():
    proflevel = get_level()
    profgame = generate_integer(proflevel)
    return profgame

def get_level():
    while True:
        try:
            level_digit = int(input("Level: "))
            if level_digit == 1 or level_digit == 2 or level_digit == 3:
                return level_digit
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        lowend = 0
        highend = 9
    elif level == 2:
        lowend = 10
        highend = 99
    elif level == 3:
        lowend = 100
        highend = 999
    
    x = [random.randint(lowend, highend) for _ in range(0, 10)]
    y = [random.randint(lowend, highend) for _ in range(0, 10)]

    i = 0
    score = 0
    while i < 10:
        attempts = 0
        while True:
            try:
                while attempts < 3:
                    guess = int(input(f"{x[i]} + {y[i]} = "))
                    if guess != x[i] + y[i]:
                        raise ValueError
                    elif guess == x[i] + y[i]:
                        i += 1
                        score += 1
                        break
                break
            except ValueError:
                print("EEE")
                attempts += 1
                if attempts == 3:
                    print(f"{x[i]} + {y[i]} = {x[i] + y[i]}")
                    i += 1
                    break
        if i > 9:
            print(f"Score: {score}")
            break

if __name__ == "__main__":
    main()