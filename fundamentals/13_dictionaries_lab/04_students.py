students_list = []
selected_students_map = {}

while True:
    student_info = input()

    if ":" in student_info:
        name, id_, course = student_info.split(":")

        students_list.append({'name': name, 'id_': id_, 'course': course.replace(" ", "")})

    else:
        for student in students_list:
            if student['course'] == student_info.replace("_", ""):
                selected_students_map[student['id_']] = student['name']
        break

for key, value in selected_students_map.items():
    print(f"{value} - {key}")
