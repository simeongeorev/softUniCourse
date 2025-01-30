hours_exam = int(input())
minutes_exam_str = str(input())
hours_arrival = int(input())
minutes_arrival_str = str(input())

minutes_exam = int(minutes_exam_str)
minutes_arrival = int(minutes_arrival_str)
# Студент трябва да отиде на изпит в определен час (например в 9:30 часа).
# Той идва в изпитната зала в даден час на пристигане (например 9:40).
# Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин час преди това.
# Ако е пристигнал по-рано повече от 30 минути, той е подранил. Ако е дошъл след часа на изпита, той е закъснял.
# Напишете програма, която прочита време на изпит и време на пристигане и отпечатва дали студентът е дошъл навреме,
# дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.

# exact scenario
if minutes_exam == minutes_arrival and hours_exam == hours_arrival:
    print("On time")

# positive scenario
if minutes_exam >= 30 and hours_arrival == hours_exam:
    if minutes_exam - minutes_arrival > 0:
        print("On time")
        print(f"{minutes_exam - minutes_arrival} minutes before the start")
    if minutes_exam - minutes_arrival == 0:
        print("On time")

# positive scenario < 30
allowed_hours = 0
allowed_minutes = 0
if minutes_exam < 30:
    allowed_hours = hours_exam - 1
    allowed_minutes = 60 - abs(minutes_exam - 30) # 60

if hours_arrival == allowed_hours and minutes_arrival >= allowed_minutes and minutes_arrival - allowed_minutes <= 30:
    print("On time")
    print(f"{(minutes_exam + 60) - minutes_arrival} minutes before the start")



# all the lates
if hours_arrival == hours_exam and minutes_arrival > minutes_exam:
    print("Late")
    print(f"{minutes_arrival - minutes_exam} minutes after the start")
if hours_arrival > hours_exam:
    print("Late")
    if minutes_arrival - minutes_exam < 10:
        print(f"{hours_arrival - hours_exam}:{(minutes_arrival - minutes_exam):02d} hours after the start")
    else:
        print(f"{hours_arrival - hours_exam}:{(minutes_arrival - minutes_exam)} hours after the start")

# early
# minutes early
# if hours_arrival == allowed_hours and :

# same hours early
if hours_arrival == hours_exam and minutes_arrival + 30 < minutes_exam:
    print("Early")
    print(f"{minutes_exam - minutes_arrival} minutes before the start")

# 1:00 - 1:59 early
if hours_arrival == hours_exam - 1 and minutes_arrival <= minutes_exam:
    print("Early")
    if minutes_exam - minutes_arrival < 10:
        print(f"{hours_exam - hours_arrival}:{(minutes_exam - minutes_arrival):02d} hours before the start")
    else:
        print(f"{hours_exam - hours_arrival}:{minutes_exam - minutes_arrival} hours before the start")



