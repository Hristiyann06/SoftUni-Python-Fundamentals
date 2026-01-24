N = int(input())

num_sum = 0

for letter in range(1, N + 1):
    letter = input()
    letter_num = ord(letter)
    num_sum += letter_num

print(f'The sum equals: {num_sum}')