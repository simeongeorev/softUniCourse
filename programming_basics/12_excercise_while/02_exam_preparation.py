number_of_bad_grades_to_fail = int(input())

average_grade = 0
number_of_tasks = 0
number_of_current_bad_grades = 0
grades_total = 0
last_task_name = ""

task_name = input()

while task_name != "Enough":
    task_grade = int(input())

    number_of_tasks += 1
    grades_total += task_grade
    average_grade = grades_total / number_of_tasks

    if task_grade <= 4:
        number_of_current_bad_grades += 1

    if number_of_current_bad_grades == number_of_bad_grades_to_fail:
        print(f"You need a break, {number_of_bad_grades_to_fail} poor grades.")
        break

    last_task_name = task_name
    task_name = input()

else:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {number_of_tasks}")
    print(f"Last problem: {last_task_name}")



