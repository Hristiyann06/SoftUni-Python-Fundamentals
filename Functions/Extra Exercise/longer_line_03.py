from math import floor 

def longer_line():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x3 = float(input())
    y3 = float(input())
    x4 = float(input())
    y4 = float(input())

    first_line = ((abs(x1) + abs (y1)) + (abs(x2) + abs(y2)))
    second_line = ((abs(x3) + abs (y3)) + (abs(x4) + abs(y4)))

    if first_line > second_line:
        if (abs(x1) + abs (y1)) <= (abs(x2) + abs(y2)):
            return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
        else:
            return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"
    elif first_line < second_line:
        if (abs(x3) + abs (y3)) <= (abs(x4) + abs(y4)):
            return f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})"
        else:
            return f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})"
    else:
        return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
    
print(longer_line())


