loading_percent = int(input())


def loading_bar(percent):
    completed = percent // 10
    remaining = 10 - completed

    bar = "[" + "%" * completed + "." * remaining + "]"

    if percent < 100:
        print(f"{percent}% {bar}")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(bar)


loading_bar(loading_percent)