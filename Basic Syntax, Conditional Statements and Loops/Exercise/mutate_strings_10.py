first_string = input()
second_string = input()

result_string = ""

for i in range(len(first_string)):
    if first_string[i] == second_string [i]:
        continue
    result_string = second_string[:(i + 1)] + first_string[(i + 1):]
    if first_string == second_string:
        break
    print(result_string)