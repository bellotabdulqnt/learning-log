amount = 50
while amount > 0:
    print(f"Amount Due: {amount}")
    pay = int(input("Insert Coin: "))
    if pay == 5 or pay == 10 or pay == 25:
        amount = amount - pay
    else:
        continue
print(f"Change Owed: {-amount}")