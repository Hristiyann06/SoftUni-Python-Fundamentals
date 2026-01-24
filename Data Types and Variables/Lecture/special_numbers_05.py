n = int(input())
special = None

for i in range(1, n + 1):
    sum = 0
    if i > 10:
        i = str(i)
        for digit in i:
            digit = int(digit)
            sum = sum + digit
            if sum == 5 or sum == 7 or sum == 11:
                special = True
            else:
                special = False
    else:
        i = int(i)
        if i == 5 or i == 7:
            special = True
        else:
            special = False

    if special:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")