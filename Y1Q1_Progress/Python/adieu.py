import inflect
p = inflect.engine()
adieunames = []
while True:
    try:
        adieunames.append(input("Name: "))
    except EOFError:
        break
print(f"Adieu, adieu, to {p.join(adieunames)}")