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

exam_whole_time_in_minutes = hours_exam * 60 + minutes_exam
arrival_whole_time_in_minutes = hours_arrival * 60 + minutes_arrival

allowed_whole_time_in_minutes = exam_whole_time_in_minutes - 30

# on time
if arrival_whole_time_in_minutes == exam_whole_time_in_minutes:
    print("On time")
# on time with the allowance
elif allowed_whole_time_in_minutes <= arrival_whole_time_in_minutes < exam_whole_time_in_minutes:
    print("On time")
    print(f"{exam_whole_time_in_minutes - arrival_whole_time_in_minutes} minutes before the start")
# late
elif arrival_whole_time_in_minutes > exam_whole_time_in_minutes:
    minutes_late = arrival_whole_time_in_minutes - exam_whole_time_in_minutes
    if minutes_late < 60:
        print("Late")
        print(f"{minutes_late} minutes after the start")
    elif minutes_late >= 60:
        print("Late")
        hours_late = minutes_late // 60
        formatted_minutes_left = minutes_late % 60
        if formatted_minutes_left < 10:
            print(f"{hours_late}:{formatted_minutes_left:02d} hours after the start")
        else:
            print(f"{hours_late}:{formatted_minutes_left} hours after the start")
# early
elif arrival_whole_time_in_minutes < allowed_whole_time_in_minutes:
    minutes_early = exam_whole_time_in_minutes - arrival_whole_time_in_minutes
    if minutes_early < 60:
        print("Early")
        print(f"{minutes_early} minutes before the start")
    elif minutes_early >= 60:
        print("Early")
        hours_early = minutes_early // 60
        formatted_minutes_left = minutes_early % 60
        if formatted_minutes_left < 10:
            print(f"{hours_early}:{formatted_minutes_left:02d} hours before the start")
        else:
            print(f"{hours_early}:{formatted_minutes_left} hours before the start")


