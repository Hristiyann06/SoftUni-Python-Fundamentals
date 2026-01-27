factor = int(input())
lenght = int(input())

list = []

for i in range(1, lenght + 1):
    number = factor * i
    list.append(number)

print(list)