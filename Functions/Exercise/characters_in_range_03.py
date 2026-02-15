def chars_between(a, b):
    result = []

    start = ord(a)
    end = ord(b)

    for i in range(start + 1, end):
        result.append(chr(i))

    return " ".join(result)


first = input()
second = input()

print(chars_between(first, second))