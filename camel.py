Input = input("Write in camel here:")

word = ''.join(['_' + char.lower() if char.isupper() else char for char in Input])

if word.startswith("_"):
    word = word[1:]

print(word)