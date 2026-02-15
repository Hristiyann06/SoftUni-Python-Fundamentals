nums = input().split()

evens = list(filter(lambda x: int(x) % 2 == 0, nums))
evens = [int(x) for x in evens]

print(evens)