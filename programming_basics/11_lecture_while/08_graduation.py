student_name = input()

nth_grade = 1
year_failed = 0
total_grade = 0

while nth_grade <= 12:
    annual_score = float(input())
    if 0 < annual_score < 4:
        year_failed += 1
        if year_failed == 2:
            print(f"{student_name} has been excluded at {nth_grade} grade")
            break
        continue
    elif 6 >= annual_score >= 4 :
        total_grade += annual_score
    nth_grade += 1
else:
    average_grade = total_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")


