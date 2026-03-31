encrypted_message = input()

while True:
    command = input()
    if command == "Decode":
        break

    operations = command.split("|")

    if operations[0] == "Move":
        num = int(operations[1])
        encrypted_message = encrypted_message[num:] + encrypted_message[:num]
    elif operations[0] == "Insert":
        index, value = int(operations[1]), operations[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif operations[0] == "ChangeAll":
        substring, replacment = operations[1], operations[2]
        encrypted_message = encrypted_message.replace(substring, replacment)


print(f"The decrypted message is: {encrypted_message}")
