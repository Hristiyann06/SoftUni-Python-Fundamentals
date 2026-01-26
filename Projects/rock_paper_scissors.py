import random

def prRed(s): print("\033[91m {}\033[00m".format(s))
def prGreen(s): print("\033[92m {}\033[00m".format(s))
def prYellow(s): print("\033[93m {}\033[00m".format(s))
def prCyan(s): print("\033[96m {}\033[00m".format(s))

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_score = 0
computer_score = 0


while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("Invalid input. Try again...")
        continue

    computer_random_number = random.randint(1, 3)

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print("Computer chose:", computer_move)

    if (player_move == rock and computer_move == scissors) or \
       (player_move == paper and computer_move == rock) or \
       (player_move == scissors and computer_move == paper):
        player_score += 1
        prGreen("You win!")
        prCyan(f"Score board: You: {player_score} Computer: {computer_score} ")
        
    elif player_move == computer_move:
        prYellow("Draw!")
    else:
        computer_score += 1
        prRed("You lose!")
        prCyan(f"Score board: You: {player_score} Computer: {computer_score} ")

    choice = input("Press Enter to play again, or type 'quit' to quit: ").strip().lower()
    if choice == "quit":
        print("Thanks for playing 👋")
        break