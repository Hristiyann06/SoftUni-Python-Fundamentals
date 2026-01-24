pattern = int(input())

for pattern in range(1 , pattern + 1):
    print("*" * pattern)

for i in range(pattern -1, 0, -1):
    print("*" * i)
    