import re

def main():
    try:
        print(validate(input("IPv4 Address: ")))
    except (AttributeError, ValueError):
        print("False")


def validate(ip):
    ipdigit = re.search(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip)
    first, second, third, fourth = int(ipdigit.group(1)), int(ipdigit.group(2)), int(ipdigit.group(3)), int(ipdigit.group(4))
    if first<=255 and second<=255 and third<=255 and fourth<=255:
        if all(
            (len(ipdigit.group(i+1))==1 and int(ipdigit.group(i+1))<10) or 
            (len(ipdigit.group(i+1))==2 and 10<=int(ipdigit.group(i+1))<100) or 
            (len(ipdigit.group(i+1))==3 and 100<=int(ipdigit.group(i+1))<=255) 
            for i in range(4)
                ):
            verdict = True
        else:
            verdict = False
    else:
        verdict = False
    return verdict


if __name__ == "__main__":
    main()