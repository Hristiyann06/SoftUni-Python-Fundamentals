n = int(input())
word = input()
strings = []

for _ in range (1, n + 1):
    current_string = input()
    strings.append(current_string)
print(strings)

for i in range (len(strings) -1, -1, -1):
    if word not in strings[i]:
        strings.remove(strings[i])
print(strings)