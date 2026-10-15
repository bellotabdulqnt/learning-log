words = input("Input: ")
for i in words:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        words = words.replace(i, "")
print(f"Output: {words}")