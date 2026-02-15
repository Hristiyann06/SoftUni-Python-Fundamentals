def data_type():
    type = input()
    data = input()
    if type == "int":
        return int(data) * 2
    elif type == "real":
        return f"{float(data) * 1.5:.2f}"
    elif type == "string":
        return f"${data}$"
    else:
        return "Invaldid data"
    

print(data_type())