from validator_collection import validators, checkers, errors

mail = input("What's your email address? ")
if checkers.is_email(mail) == True and not " " in mail:
    print("Valid")
else:
    print("Invalid")