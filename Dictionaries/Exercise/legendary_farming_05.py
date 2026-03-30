resources = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

while True:
    line = input().split()

    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1].lower()
        
        if material in resources:
            resources[material] += quantity
            if resources[material] >= 250:
                print(f"{legendary_items[material]} obtained!")
                resources[material] -= 250
                for key in resources:
                    print(f"{key}: {resources[key]}")
                for item, count in junk.items():
                    print(f"{item}: {count}")
                exit()
        else:
            junk[material] = junk.get(material, 0) + quantity

    
