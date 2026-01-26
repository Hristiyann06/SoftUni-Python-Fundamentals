import random

computer_number = random.randint(1,100)

print("------------GUESS THE NUMBER------------")

while True:
    player_input = input("Guess the number(1 - 100)")
    if not player_input.isdigit():
        print("Invalid input. Type a number between 1 and 100.")
    
    player_number = int(player_input)

    if player_number == computer_number:
        print(f"You guessed it! The number is {computer_number}.")
        break
    elif player_number > computer_number:
        print(f"{player_number} is HIGHER than the computer's ")
    else:
        print(f"{player_number} is LOWER than the computer's")

