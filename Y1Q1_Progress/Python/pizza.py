import sys
from tabulate import tabulate
import csv
def main():
    try:
        print(tabulation(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")
    except IndexError:
        sys.exit("Too few command-line arguments")

def tabulation(filename):
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    with open(filename) as file:
        table = csv.DictReader(file)
        return tabulate(table, headers="keys", tablefmt="grid")


if __name__=="__main__":
    main()