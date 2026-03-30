phonebook = {}
line = input()

while not line.isdigit():
    name, number = line.split("-")
    phonebook[name] = number
    line = input()

for _ in range(int(line)):
    search = input()
    if search not in phonebook.keys():
        print(f"Contact {search} does not exist.")
    else:
        print(f"{search} -> {phonebook[search]}")