items= input().split("|")

grid = []
for x in items:
    grid.append(int(x))

total_items = 0

while True:
    command = input()

    if command == "Adventure over":
        break

    if command == "Switch":
        grid.reverse()

    elif "Double" in command:
        parts = command.split()
        index = int(parts[1])

        if 0 <= index < len(grid):
            grid[index] *= 2

    elif "Step" in command:
        parts = command.split("$")

        action = parts[0]
        start_index = int(parts[1])
        steps = int(parts[2])

        if 0 <= start_index < len(grid):

            if action == "Step Backward":
                position = start_index - steps
            elif action == "Step Forward":
                position = start_index + steps

            position = position % len(grid)

            total_items += grid[position]
            grid[position] = 0


for i in range(len(grid)):
    if i == len(grid) - 1:
        print(grid[i])
    else:
        print(grid[i], end=" - ")

print(f"Robo finished the adventure with {total_items} items!")