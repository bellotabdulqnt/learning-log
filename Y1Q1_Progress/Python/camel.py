def main():
    snake_case(input("camelCase: "))


def snake_case(camelcase):
    camelcase = " ".join(camelcase).split(" ")
    for camel in camelcase:
            if camel.isupper():
                camelcase = camelcase[:camelcase.index(camel)] + ["_"] + [camelcase[camelcase.index(camel)].lower()] + camelcase[((camelcase.index(camel))+1):]
    snakecased = "".join(camelcase)
    print(snakecased)


main()