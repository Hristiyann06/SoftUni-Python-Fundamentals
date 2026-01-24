n = int(input())



for messages in range(n):
    code = int(input())
    text = ""
    if code == 88:
        text = "Hello"
    elif code == 86:
        text = "How are you?"
    elif code < 88 and (not code == 86 or code == 88):
        text = "GREAT!"
    else:
        text = "Bye."

    print(text)
