string = input().split(" ")
text = ""
for word in string:
    text += word * len(word)

print(text)