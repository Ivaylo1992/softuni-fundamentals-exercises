students_count = int(input())
students_info = {}

for student in range(students_count):
    student_name = input()
    grade = float(input())

    if student_name not in students_info:
        students_info[student_name] = []

    students_info[student_name].append(grade)


for student, grade in students_info.items():
    average = sum(grade) / len(grade)
    if average >= 4.5:
        print(f"{student} -> {average:.2f}")
