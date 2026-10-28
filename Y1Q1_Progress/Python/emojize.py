import emoji as emj
emjtext = emj.emojize(input("Input: "))
emjtext_list = emjtext.split()
for word in emjtext_list:
    if word.startswith(":") and word.endswith(":"):
        wordnew = emj.emojize(word, language='alias')
        emjtext_list[emjtext_list.index(word)] = wordnew


outputtext = "".join(emjtext_list)
print(f"Output: {outputtext}")