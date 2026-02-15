def caluclations():
    type = input()
    num1 = int(input())
    num2 = int(input())
    if type == "add":
        print(int(num1 + num2))
    elif type == "subtract":
        print(int(num1 - num2))
    elif type == "multiply":
        print(int(num1 * num2))
    elif type == "divide":
        print(int(num1 / num2))
    else:
        print("Unknown operation")

caluclations()