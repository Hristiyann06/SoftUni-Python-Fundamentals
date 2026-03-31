text = input()
result = ""

for i in range(len(text) - 1):
    if text[i] != text[i + 1]:
        result += text[i]

if text:
    result += text[-1]

print(result)