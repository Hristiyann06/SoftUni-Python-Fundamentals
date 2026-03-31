first, second = input().split()

min_word = min(len(first), len(second))
total = 0

for i in range(0, min_word):
    total += ord(first[i]) * ord(second[i])

if len(first) > len(second):
    for i in range(min_word, len(first)):
        total += ord(first[i])
elif len(first) < len(second):
    for i in range(min_word, len(second)):
        total += ord(second[i])
print(total)
