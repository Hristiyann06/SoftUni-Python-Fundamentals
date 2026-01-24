budget = float(input())
flour_price_per_kg = float(input())

price_eggs_per_pack = flour_price_per_kg * 0.75
price_milk_per_liter = flour_price_per_kg * 1.25
price_milk_per_250ml = price_milk_per_liter / 4

price_per_loaf = flour_price_per_kg + price_eggs_per_pack + price_milk_per_250ml

loaves_baked = 0
colored_eggs = 0

while budget >= price_per_loaf:
    if budget < price_per_loaf:
        break
    budget -= price_per_loaf
    loaves_baked += 1
    colored_eggs += 3
    if loaves_baked % 3 == 0 and loaves_baked > 2:
        colored_eggs -= (loaves_baked - 2)
    

print(f"You made {loaves_baked} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
    