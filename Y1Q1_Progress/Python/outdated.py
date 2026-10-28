months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
months_dict = {months[i]:i+1 for i in range(len(months))}

while True:
    try:
        while True:
            old_date = input("Date: ")
            month, day, year = old_date.replace(",", "").replace("/", " ").split()
            day, year = [int(day), int(year)]
            if month.isalpha():
                month_digit = months_dict[month.lower().capitalize()]
            elif month.isnumeric():
                month_digit = int(month)
            if 1<= month_digit <= 12 and 1<= day <= 31 and year>=1 :
                break
            else:
                pass
        print(f"{year}-{month_digit:02d}-{day:02d}")
        break
    except (NameError, ValueError, KeyError):
        pass