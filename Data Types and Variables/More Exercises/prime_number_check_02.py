n = int(input())
prime = False
checker = False

for i in range(2, n):
    if n % i == 0:
        checker = True

if not checker:
    prime = True

print(prime)