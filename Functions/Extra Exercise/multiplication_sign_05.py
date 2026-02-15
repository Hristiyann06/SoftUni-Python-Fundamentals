def multiplication_sign():
    first_number = int(input())
    second_number = int(input())
    third_number = int(input())
    negative_count = 0 
    numbers = [first_number, second_number, third_number]
    for number in numbers:
        if number < 0:
            negative_count += 1
        

    if first_number == 0 or second_number == 0 or third_number == 0:
        return "zero"
    elif negative_count == 1 or negative_count == 3:
        return "negative"
    else:
        return "positive"

print(multiplication_sign())