def absolute_values():
    numbers = input().split()
    result = [abs(float(x)) for x in numbers]
    print(result)


absolute_values()