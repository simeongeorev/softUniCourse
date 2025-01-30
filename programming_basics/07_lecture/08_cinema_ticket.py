day = str(input())

if day == "Monday" or day == "Tuesday" or day == "Friday":
    rate = 12
elif day == "Wednesday" or day == "Thursday":
    rate = 14
elif day == "Saturday" or day == "Sunday":
    rate = 16

print(rate)



