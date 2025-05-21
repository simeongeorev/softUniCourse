lessons_schedule = input().split(", ")

while True:

    command = input()

    if command == "course start":
        break

    command_list = command.split(":")
    lesson_title = command_list[1]
    lesson_exercise = f"{lesson_title}-Exercise"

    if "Add" in command_list:
        if lesson_title not in lessons_schedule:
            lessons_schedule.append(lesson_title)

    elif "Insert" in command_list:
        index = int(command_list[2])
        if lesson_title not in lessons_schedule:
            lessons_schedule.insert(index, lesson_title)

    elif "Remove" in command_list:
        if lesson_title in lessons_schedule:
            lessons_schedule.remove(lesson_title)
        if lesson_exercise in lessons_schedule:
            lessons_schedule.remove(lesson_exercise)

    elif "Swap" in command_list:
        lesson_title_2 = command_list[2]
        lesson_exercise_2 = f"{lesson_title_2}-Exercise"
        if lesson_title in lessons_schedule and lesson_title_2 in lessons_schedule:
            index_of_lesson_1 = lessons_schedule.index(lesson_title)
            index_of_lesson_2 = lessons_schedule.index(lesson_title_2)

            lessons_schedule[index_of_lesson_1], lessons_schedule[index_of_lesson_2] = \
                lessons_schedule[index_of_lesson_2], lessons_schedule[index_of_lesson_1]

            if lesson_exercise in lessons_schedule:
                lessons_schedule.remove(lesson_exercise)
                lessons_schedule.insert(index_of_lesson_2 + 1, lesson_exercise)
            if lesson_exercise_2 in lessons_schedule:
                lessons_schedule.remove(lesson_exercise_2)
                lessons_schedule.insert(index_of_lesson_1 + 1, lesson_exercise_2)

    elif "Exercise" in command_list:
        # lesson exists
        if lesson_title in lessons_schedule:
            index_of_lesson = lessons_schedule.index(lesson_title)

            # lesson exists but it has no exercise
            if lesson_exercise not in lessons_schedule:
                lessons_schedule.insert(index_of_lesson + 1, lesson_exercise)

        # lesson doesn't exist
        else:
            lessons_schedule.append(lesson_title)
            lessons_schedule.append(lesson_exercise)

for i in range(len(lessons_schedule)):
    print(f"{i + 1}.{lessons_schedule[i]}")
