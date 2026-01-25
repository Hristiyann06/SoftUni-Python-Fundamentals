key = int(input())
n = int(input())
result = ''

for _ in range(1, n +1):
    letter = input()
    num = ord(letter)
    result += chr(num + key)

print(result)
