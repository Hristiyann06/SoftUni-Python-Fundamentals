snowballs = int(input())
highest_value = 0
highest_quality = 0
highest_weight = 0
highest_time_needed = 0
quality = 0

for snowball in range(1, snowballs + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    value = (weight // time_needed) ** quality 
    if value > highest_value:
        highest_value = value
        highest_quality = quality
        highest_weight = weight
        highest_time_needed = time_needed

print(f'{highest_weight} : {highest_time_needed} = {highest_value} ({highest_quality})')
