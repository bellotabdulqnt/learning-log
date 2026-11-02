def main():
    while True:
        try:
            gauge_level = convert(input("Fraction: "))
            print(gauge(gauge_level))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x, y = fraction.split("/")
    X, Y = [int(x), int(y)]
    return X/Y



def gauge(percentage):
    if 0 <= percentage <= 0.01:
        return "E"
    elif 0.99 <= percentage <= 1:
        return "F"
    elif percentage < 0 or percentage > 1:
        raise ValueError
    else:
        return f"{int(100*percentage)}%"



if __name__ == "__main__":
    main()