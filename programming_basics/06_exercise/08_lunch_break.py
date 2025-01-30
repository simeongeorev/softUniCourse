# 08_lunch_break
# По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма,
# с която ще разберете дали имате достатъчно време да изгледате епизода. По време на почивката отделяте време за обяд и време за отдих.
# Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
# Вход
# От конзолата се четат 3 реда:
# 1. Име на сериал – текст
# 2. Продължителност на епизод – цяло число в диапазона [10… 90]
# 3. Продължителност на почивката – цяло число в диапазона [10… 120]
import math

series_name = str(input())

episode_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration * (1 / 8)
chill_duration = break_duration * (1 / 4)

free_time_in_break = break_duration - (lunch_duration + chill_duration)
time_left_in_break = free_time_in_break - episode_duration

if time_left_in_break >= 0:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(time_left_in_break)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(time_left_in_break * -1)} more minutes.")