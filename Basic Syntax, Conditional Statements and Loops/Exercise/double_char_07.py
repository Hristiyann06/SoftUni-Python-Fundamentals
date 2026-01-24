while True:
    string_given = (input())
    double_ch = ""
    if string_given == "End":
        break
    if string_given == "SoftUni":
        continue
    for ch in string_given:
        double_ch += ch * 2
    print(double_ch)
