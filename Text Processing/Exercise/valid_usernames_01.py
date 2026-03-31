usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16:
        not_valid = False
        for ch in username:
            if not ch.isalpha() and not ch.isdigit() and ch != "-" and ch != "_":
                not_valid = True
                break
        if not not_valid:
            print(username)
