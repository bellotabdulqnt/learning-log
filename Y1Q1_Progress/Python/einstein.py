def main():
    e = energy(float(input("m: ")))
    print(e)

def energy(m):
    c =  300000000
    return m * pow(float(c), 2)
main()