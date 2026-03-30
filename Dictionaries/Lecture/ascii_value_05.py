text = input().split(", ")

dictionary = {}

for symbol in text:
    dictionary[symbol] = ord(symbol)

print(dictionary)