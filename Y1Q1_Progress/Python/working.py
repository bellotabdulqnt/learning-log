import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        hour12 = re.search(r"^(\d{1,2})(?:\:(\d{2}))? (AM|PM) to (\d{1,2})(?:\:(\d{2}))? (AM|PM)$", s)
        firsthour, firstmin, firstampm, secondhour, secondmin, secondampm = (
        int(hour12.group(1)),
        hour12.group(2),
        hour12.group(3),
        int(hour12.group(4)),
        hour12.group(5),
        hour12.group(6),
        )
        firstmin = int(firstmin) if firstmin is not None else 0
        secondmin = int(secondmin) if secondmin is not None else 0
        if 1<=firsthour<=12 and 1<=secondhour<=12 and firstmin<60 and secondmin<60:
            firsthour = (firsthour-12 if firsthour == 12 else firsthour) if firstampm == "AM" else (firsthour+12 if firsthour < 12 else firsthour)
            secondhour = (secondhour - 12 if secondhour == 12 else secondhour) if secondampm == "AM" else (secondhour + 12 if secondhour < 12 else secondhour)
        else:
            raise(ValueError)
        return f"{firsthour:02}:{firstmin:02} to {secondhour:02}:{secondmin:02}"
    except AttributeError:
        raise(ValueError)


if __name__ == "__main__":
    main()