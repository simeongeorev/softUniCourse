# Иван решава да подобри Световния рекорд по плуване на дълги разстояния. На конзолата се въвежда рекордът
# в секунди, който Иван трябва да подобри, разстоянието в метри, което трябва да преплува и времето в секунди,
# за което плува разстояние от 1 м. Да се напише програма, която изчислява дали се е справил със задачата,
# като се има предвид, че: съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
# Когато се изчислява колко пъти Иван ще се забави, в резултат на съпротивлението на водата,
# резултатът трябва да се закръгли надолу до най-близкото цяло число.

# Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.

# 1. Рекордът в секунди – реално число;
# 2. Разстоянието в метри – реално число;
# 3. Времето в секунди, за което плува разстояние от 1 м. - реално число.

import math

current_record = float(input())
distance = float(input())
time_to_swim_1m = float(input())

time_to_swim_the_whole_distance = distance * time_to_swim_1m

time_to_swim_the_whole_distance = time_to_swim_the_whole_distance + (distance // 15) * 12.5
round(time_to_swim_the_whole_distance)

if time_to_swim_the_whole_distance < current_record:
    print(f" Yes, he succeeded! The new world record is {time_to_swim_the_whole_distance:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_to_swim_the_whole_distance - current_record:.2f} seconds slower.")