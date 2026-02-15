n = int(input())


def tribonacci(num):
    sequence = [1, 1, 2]

    if num == 1:
        print(1)
        return
    elif num == 2:
        print(1, 1)
        return
    elif num == 3:
        print(1, 1, 2)
        return

    for _ in range(3, num):
        next_num = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(next_num)

    print(*sequence)


tribonacci(n)