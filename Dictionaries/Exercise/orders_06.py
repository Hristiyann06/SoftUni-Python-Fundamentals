dictionary = {}

while True:
    command = input()
    if command == "buy":
        break
    line = command.split()
    name, price, quantity = line[0], float(line[1]), int(line[2])
    
    if name not in dictionary:
        dictionary[name] = {"product_price": price, "product_quantity": quantity}
    else:
        dictionary[name]["product_price"] = price
        dictionary[name]["product_quantity"] += quantity

for name, data in dictionary.items():
    total = data["product_price"] * data["product_quantity"]
    print(f"{name} -> {total:.2f}")