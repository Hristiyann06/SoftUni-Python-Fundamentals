number = int(input())
number_as_string = str(number)

def odd_and_even_sum():
    odd_sum = 0
    even_sum = 0
    for i in range(len(number_as_string)):
        if int(number_as_string[i]) % 2 == 0:
            even_sum += int(number_as_string[i])
        else:
            odd_sum += int(number_as_string[i])
            
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


print(odd_and_even_sum())