from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fontlist = figlet.getFonts()


if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fontlist))
elif len(sys.argv) == 3 and sys.argv[2] in fontlist and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

figtext = input("Input: ")
print(figlet.renderText(figtext))