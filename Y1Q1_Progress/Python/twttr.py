def main():
    words = shorten(input("Input: "))
    print(f"Output: {words}")


def shorten(word):
    for i in word:
        if i in list("aeiouAEIOU"):
            word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()