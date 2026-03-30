n = int(input())
student_academy = {}
grades_count = {}

for _ in range(n):
    student_name = input()
    grade = float(input())
    
    if student_name not in student_academy:
        student_academy[student_name] = grade
        grades_count[student_name] = 1
    else:
        student_academy[student_name] += grade
        grades_count[student_name] += 1

for student_name, total_grade in student_academy.items():
    average = total_grade / grades_count[student_name]
    if average >= 4.50:
        print(f"{student_name} -> {average:.2f}")


