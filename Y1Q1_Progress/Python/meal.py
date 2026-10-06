def main():
    meal = convert(input("What time is it? "))
    if 7 <= meal <= 8:
        print("breakfast time")
    elif 12 <= meal <= 13:
        print("lunch time")
    elif 18 <= meal <= 19:
        print("dinner time")

    
def convert(time):
    if time.endswith("AM") or time.endswith("PM"):
        hours, minutes, meridiem = time.replace(" ", ":").split(":")
        if meridiem == "AM":
            a = 1
            p = 0
        elif meridiem == "PM":
            a = 0
            p = 1
        hours = 12 * p + (a + p) * (float(hours) % 12)
    else:
        hours, minutes = time.split(":")
    ttime = float(hours) + (float(minutes)/60)
    return ttime

if __name__ == "__main__":
    main()
