first_number = int(input())
second_number = int(input())

def factorial_division ():
    first_factorial = 1
    second_factorail = 1
    for factors in range(1, first_number + 1):
        first_factorial *= factors
    for factors in range(1, second_number + 1):
        second_factorail *= factors
    
    division = first_factorial / second_factorail
    return f"{division:.2f}"

print(factorial_division())