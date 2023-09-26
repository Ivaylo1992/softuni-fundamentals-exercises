from math import ceil

students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())
max_attendance = 0
max_bonus = 0

for student in range(students_count):
    attendance = int(input())
    student_bonus = (1.0 * attendance / lectures_count) * (5 + additional_bonus)
    if student_bonus >= max_bonus:
        max_bonus = student_bonus
        max_attendance = attendance


print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")