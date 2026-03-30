dictionary = {}

string = input()

for char in string:
    if char != " ":
        dictionary[char] = dictionary.get(char, 0) + 1

for char, count in dictionary.items():
    print(f"{char} -> {count}")
