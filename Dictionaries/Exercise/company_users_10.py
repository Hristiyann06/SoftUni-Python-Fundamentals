company_users = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, employee_id = command.split(" -> ")
    company_users[company_name] = company_users.get(company_name, [])
    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)

for key, value in company_users.items():
    print(key)
    for id in value:
        print(f"-- {id}")