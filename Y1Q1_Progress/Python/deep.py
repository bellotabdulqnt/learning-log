def main():
    x = question()
    if x == "42" or x == "forty two":
        print("Yes")
    else:
        print("No")




def question():
    deepq = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if deepq != "42":
        deepql = list(deepq)
        for i in deepql:
            if i == "-" or i == " ":
                deepql.pop(deepql.index(i))
            else:
                pass
        deepqla = "".join(deepql[0:5])
        deepqlb = "".join(deepql[5:])
        if deepqlb != "":
            deepq = deepqla + " " + deepqlb
        else:
            deepq = deepqla
    else:
        pass
    print(deepq.lower())
    return deepq.lower()

main()