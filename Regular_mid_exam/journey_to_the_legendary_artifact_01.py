initial_energy = float(input())

artifact_pieces = 0
mountain_count = 0

while True:
    terrain = input()

    if terrain == "Journey ends here!":
        break

    if terrain == "mountain":
        initial_energy -= 10
        mountain_count += 1

        if mountain_count % 3 == 0:
            artifact_pieces += 1

    elif terrain == "desert":
        initial_energy -= 15

    elif terrain == "forest":
        initial_energy += 7

    if initial_energy <= 0 or artifact_pieces == 3:
        break


if artifact_pieces == 3:
    print(f"The character reached the legendary artifact with {initial_energy:.2f} energy left.")
elif initial_energy <= 0:
    print("The character is too exhausted to carry on with the journey.")
else:
    print(f"The character could not find all the pieces and needs {3 - artifact_pieces} more to complete the legendary artifact.")