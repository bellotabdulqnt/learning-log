import re

def main():
    try:
        print(parse(input("HTML: ")))
    except AttributeError:
        print("None")


def parse(s):
    ytembed = re.search(r"^(?:<iframe).*? (?:src\=\"https?://)((?:www.)?youtube.com/embed/\w{11})\".*?\>(?:</iframe>)$", s)
    ytlink = re.sub(r"(?:www.)?youtube.com/embed", "youtu.be", ytembed.group(1))
    return f"https://{ytlink}"


if __name__ == "__main__":
    main()