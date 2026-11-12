import csv
import sys
try:
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    with open(f"{sys.argv[1]}") as old, open(f"{sys.argv[2]}", "w", newline="") as new:
        before = csv.DictReader(old)
        after = csv.DictWriter(new, fieldnames=["first", "last", "house"])
        after.writeheader()
        newdicts = []
        for row in before:
            last, first = row["name"].split(",")
            first = first.lstrip()
            after.writerow({"first":first, "last":last, "house":row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
except IndexError:
    sys.exit("Too few command-line arguments")