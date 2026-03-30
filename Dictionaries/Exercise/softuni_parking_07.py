register = {}
n = int(input())
for _ in range (n):
    command = input()
    line = command.split()
    if len(line) >= 2:
        username = line[1]
        license_number = line[2] if len(line) >= 3 else None
        
        if line[0] == "register" and username not in register:
            register[username] = license_number
            print(f"{username} registered {register[username]} successfully")
        elif line[0] == "register":
            print(f"ERROR: already registered with plate number {register[username]}")

        if line[0] == "unregister" and username not in register:
            print(f"ERROR: user {username} not found")
        elif line[0] == "unregister" and username in register:
            del register[username]
            print(f"{username} unregistered successfully")

for key, value in register.items():
    print(f"{key} => {value}")