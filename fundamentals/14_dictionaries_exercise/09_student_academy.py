students_info = {}
n_students = int(input())

for _ in range(n_students):
    student_name = input()
    student_grade = float(input())

    if student_name not in students_info.keys():
        students_info[student_name] = []
    students_info[student_name] += [student_grade]

for student, grade in students_info.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")