decorations_quantity = int(input())
days_until_Christmas = int(input())

ornament_set_price = 2
ornament_set_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17

total_cost = 0
total_points = 0

for days in range(1, days_until_Christmas + 1):
    if days % 11 == 0:
        decorations_quantity += 2

    if days % 2 == 0:
        total_cost += ornament_set_price * decorations_quantity
        total_points += ornament_set_points
        
    if days % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * decorations_quantity
        total_points += (tree_skirt_points + tree_garland_points)
        
    if days % 5 == 0:
        total_cost += tree_lights_price * decorations_quantity
        total_points += tree_lights_points
        
    if days % 15 == 0:
        total_points += 30

    if days % 10 == 0:
        total_points -= 20
        total_cost += (tree_skirt_price + tree_garland_price + tree_lights_price)
        
if days_until_Christmas % 10 == 0:
    total_points -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_points}")