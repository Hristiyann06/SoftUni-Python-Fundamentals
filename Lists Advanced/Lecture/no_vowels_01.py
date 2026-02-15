text = input()

vowels = "aouei"
result = ""

for ch in text:
    if ch.lower() not in vowels:
        result += ch

print(result)
