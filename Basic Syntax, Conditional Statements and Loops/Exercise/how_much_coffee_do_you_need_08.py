coffee_needed = 0

while True:
    event = input()
    if event == "coding" or event == "dog" or event == "cat" or event == "movie":
        coffee_needed += 1
    if event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        coffee_needed += 2
    if event == "END":
        if coffee_needed <= 5:
            print(coffee_needed)
            break
        else:
            print("You need extra sleep")
            break