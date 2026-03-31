ban_list = input().split(", ")
text = input()

for ban in ban_list:
    if ban in text:
        text = text.replace(ban, "*" * len(ban))

print(text)