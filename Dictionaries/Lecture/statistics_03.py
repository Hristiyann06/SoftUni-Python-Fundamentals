products = {}

while True:
    command = input()
    if command == "statistics":
        break
    
    name, qty = command.split(": ")
    qty = int(qty)
    
    products[name] = products.get(name, 0) + qty

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
