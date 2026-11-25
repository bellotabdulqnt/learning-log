from datetime import date
import inflect
import re
import sys

def main():
    try:
        p = inflect.engine()
        dateofbirth = input("Date of Birth: ")
        minofbirth = minutegrab(dateofbirth)
        print(p.number_to_words(minofbirth).capitalize(), "minutes")
    except (AttributeError, ValueError):
        sys.exit("Invalid date")


def minutegrab(season):
    bdate = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", season)
    byear, bmonth, bday = int(bdate.group(1)), int(bdate.group(2)), int(bdate.group(3))
    birthday = date(byear, bmonth, bday)
    today = date.today()
    diff = abs(today - birthday)
    return round(1440*diff.days)


if __name__ == "__main__":
    main()