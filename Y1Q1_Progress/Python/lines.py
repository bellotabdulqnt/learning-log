import sys
def main():
    try:
        print(linecounter(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")
    except IndexError:
        sys.exit("Too few command-line arguments")

def linecounter(filename):
    i=0
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif not filename.endswith(".py"):
        sys.exit("Not a Python file")

    with open(filename) as file:
        for row in file:
            if row.lstrip().startswith("#") or row=="\n":
                pass
            else:
                i+=1
    return i


if __name__=="__main__":
    main()