from math import floor

def center_point():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    if (abs(x1) + abs (y1)) < (abs(x2) + abs(y2)):
        return f"({floor(x1)}, {floor(y1)})"
    elif (abs(x1) + abs (y1)) > (abs(x2) + abs(y2)):
        return f"({floor(x2)}, {floor(y2)})"
    else:
        return f"({floor(x1)}, {floor(y1)})"

print(center_point())


