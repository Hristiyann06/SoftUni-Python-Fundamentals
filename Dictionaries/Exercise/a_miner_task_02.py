dictionary = {}

while True:
    command = input()
    if command == "stop":
        break
    item = command
    quantity = int(input())
    dictionary[item] = dictionary.get(item, 0) + quantity

for resource, value in dictionary.items():
    print(f"{resource} -> {value}")