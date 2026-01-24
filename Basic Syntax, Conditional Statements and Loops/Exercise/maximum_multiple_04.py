divisor = int(input())
boundary = int(input())
max_multiple = 0


for i in range(0, boundary +1):
    if i % divisor == 0 and i > max_multiple:
        max_multiple = i

print(max_multiple)