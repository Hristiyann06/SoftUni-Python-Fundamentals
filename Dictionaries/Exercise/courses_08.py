courses = {}
while True:
    command = input()
    if command == "end":
        break
    line = command.split(":")
    course_name = line[0].strip()
    student_name = line[1].strip()
    
    if course_name in courses:
        courses[course_name].append(student_name)
    else:
        courses[course_name] = [student_name]

for key, name in courses.items():
    print(f"{key}: {len(name)}")
    for i in name:
        print(f"-- {i}")
