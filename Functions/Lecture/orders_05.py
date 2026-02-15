product = input()
quantity = int(input())

def order():
    if product == "coffee":
        return f'{quantity * 1.50:.2f}'
    elif product == "water":
        return f'{quantity * 1.00:.2f}'
    elif product == "coke":
        return f'{quantity * 1.40:.2f}'
    elif product == "snacks":
        return f'{quantity * 2.00:.2f}'
    else:
        return "Invalid product"
    
print(order())