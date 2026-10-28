groceries = {}
while True:
    try:
        food = input().upper()
        food_dict = {food : 1}
        if food in groceries.keys():
            groceries[food] += 1
        else:
            groceries.update(food_dict)
    except EOFError:
        break

for item in sorted(groceries.keys()):
    print(groceries[item], item)