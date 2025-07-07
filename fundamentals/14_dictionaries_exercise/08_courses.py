courses_dict = {}

while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")
    if course_name not in courses_dict.keys():
        courses_dict[course_name] = []
    courses_dict[course_name] += [student_name]

for course_name, student_names in courses_dict.items():
    print(f"{course_name}: {len(student_names)}")
    for student in student_names:
        print(f"-- {student}")