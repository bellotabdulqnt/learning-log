def main():
    a = convert(input("Convert: "))
    print(a)

def convert(facetext):
    facetext = facetext.replace(":)", "🙂").replace(":(", "🙁")     

    return facetext

main()