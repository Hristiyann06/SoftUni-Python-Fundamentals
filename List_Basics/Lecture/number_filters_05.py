n = int(input())
correct_numbers = []
all_numbers = []

for _ in range(1, n + 1):
    number = int(input())
    all_numbers.append(number)

command = input()
for number in all_numbers:
    if command == "positive":
        if number >= 0:
            correct_numbers.append(number)
    elif command == "negative":
        if number < 0:
            correct_numbers.append(number)
    elif command == "even":
        if number % 2 == 0:
            correct_numbers.append(number)
    elif command == "odd":
        if number % 2 != 0:
            correct_numbers.append(number)

print(correct_numbers)
