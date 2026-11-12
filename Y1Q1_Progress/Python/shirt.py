import sys
from PIL import Image, ImageOps

#Apparently lists do not work for .endswith() if trying to check multiple endings
valid_formats = (".jpg", ".jpeg", ".png")
try:
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1][sys.argv[1].index("."):].lower() in valid_formats:
        sys.exit("Invalid input")
    elif not sys.argv[2][sys.argv[2].index("."):].lower() in valid_formats:
        sys.exit("Invalid output")
    elif sys.argv[1][sys.argv[1].index("."):].lower() != sys.argv[2][sys.argv[2].index("."):].lower():
        sys.exit("Input and output have different extensions")

    with Image.open(f"{sys.argv[1]}") as image_input, Image.open("shirt.png") as shirt:
        fitted_image = ImageOps.fit(image_input, size=shirt.size)
        fitted_image.paste(shirt, shirt)
        fitted_image.save(f"{sys.argv[2]}")
except FileNotFoundError:
    sys.exit("Input does not exist")
except IndexError:
    sys.exit("Too few command-line arguments")