import random

computer_number = random.randint(1,100)
user_number = int(input())

while computer_number != user_number:
    user_number = int(input())
    if user_number < computer_number:
        print("Higher")
    elif user_number > computer_number:
        print("Lower")
print("Correct")