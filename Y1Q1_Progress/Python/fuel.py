while True:
    try:
        x, y = input("Fraction: ").split("/")
        X, Y = [int(x), int(y)]
        if 0 <= X/Y <= 0.01:
            print("E")
            break
        elif 0.99 <= X/Y <= 1:
            print("F")
            break
        elif X>Y:
            pass
        elif X/Y < 0:
            raise ValueError
        else:
            print(f"{int(100*X/Y)}%")
            break
    except (ValueError, ZeroDivisionError):
        pass