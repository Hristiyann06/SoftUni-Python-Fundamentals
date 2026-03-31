text = input()
encrypted = ""
for ch in text:
    ascii = ord(ch) + 3
    encrypted += chr(ascii)

print(encrypted)
