numbers = input().split()
n = int(input())

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for _ in range(n):
    smallest = min(numbers)
    numbers.remove(smallest)
    
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])

print(", ".join(numbers))