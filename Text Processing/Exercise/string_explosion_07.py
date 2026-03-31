text = input()
result = ""
explosion = 0

for i in range(len(text)):
    if text[i] == ">":
        explosion += int(text[i + 1])
        result += text[i]
        continue
    elif explosion > 0:
        explosion -= 1
        continue
    result += text[i]

print(result)