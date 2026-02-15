numbers = input().split(', ')


for i in numbers:
    if i == i[::-1]:
        print(True)
    else:
        print(False)
