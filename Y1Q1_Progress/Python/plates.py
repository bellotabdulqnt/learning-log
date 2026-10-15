import string
space_punct = list(string.punctuation) + [" "]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if all(i not in space_punct for i in s) and 2 <= len(s) <= 6 and s.isalpha() or any(s[:a].isalpha() and s[a:].isdigit() and s[a] != "0" for a in range(len(s))):
        return True


main()