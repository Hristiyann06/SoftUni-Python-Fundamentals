n = int(input())
capacity = 255
current_capacity = 0

for i in range(1, n +1):
    i = int(input()) 
    if i > (capacity - current_capacity):
        print("Insufficient capacity!")
    else:
        current_capacity += i

print(current_capacity)    