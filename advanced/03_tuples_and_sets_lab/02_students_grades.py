number_of_students = int(input())
students_with_grades = {}

for _ in range(number_of_students):
    student_grade_input = input()
    student_name, student_grade = student_grade_input.split()

    if student_name not in students_with_grades.keys():
        students_with_grades[student_name] = []
    students_with_grades[student_name].append(float(student_grade))

for student, grades in students_with_grades.items():
    avg_grade = sum(grades) / len(grades)
    print(f"{student} -> {' '.join([f'{grade:.2f}' for grade in grades])} (avg: {avg_grade:.2f})")
