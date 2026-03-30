courses = {}

while True:
    user_input = input()

    if ":" not in user_input:
        course_name = user_input.replace("_", " ")

        for student in courses[course_name]:
            print(student)
        break

    student_name, student_id, course = user_input.split(":")

    if course not in courses:
        courses[course] = []

    courses[course].append(f"{student_name} - {student_id}")
