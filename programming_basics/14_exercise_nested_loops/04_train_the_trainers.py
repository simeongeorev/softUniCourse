number_of_scorers = int(input())
command = input()
presentation_counter = 0
student_total_grade = 0

while command != "Finish":
    total_score_for_presentation = 0
    presentation_counter += 1
    for i in range(number_of_scorers):
        score = float(input())
        total_score_for_presentation += score
    mid_score_for_presentation = total_score_for_presentation / number_of_scorers
    print(f"{command} - {mid_score_for_presentation:.2f}.")
    student_total_grade += mid_score_for_presentation
    command = input()
else:
    print(f"Student's final assessment is {(student_total_grade / presentation_counter):.2f}.")