people = int(input())
capacity = int(input())

operation = people // capacity
courses = operation

result = people / capacity
if not result.is_integer():
    courses +=1

print(courses)