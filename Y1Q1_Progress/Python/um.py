import re

def main():
    print(count(input("Text: ")))


def count(s):
    umcatch = re.findall(r"\bum\b", s.lower())
    return len(umcatch)


if __name__ == "__main__":
    main()