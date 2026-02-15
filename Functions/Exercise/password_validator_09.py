def validate_password(password):
    valid = True

    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        valid = False

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        valid = False

    digits = 0
    for ch in password:
        if ch.isdigit():
            digits += 1

    if digits < 2:
        print("Password must have at least 2 digits")
        valid = False

    if valid:
        print("Password is valid")


password = input()
validate_password(password)