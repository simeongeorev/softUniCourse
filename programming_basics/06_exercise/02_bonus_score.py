# 02_bonus_score
#·  Ако числото е до 100 включително, бонус точките са 5;
# · Ако числото е по-голямо от 100 и по-малко или равно на 1000, бонус точките са 20% от числото;
# · Ако числото е по-голямо от 1000, бонус точките са 10% от числото.

# o За четно число  + 1 т.
# o За число, което завършва на 5  + 2 т.

starting_points = int(input())

if starting_points <= 100:
    bonus_points = 5
    
elif starting_points <= 1000:
    bonus_points = starting_points * 0.2
    
elif starting_points > 1000:
    bonus_points = starting_points * 0.1

if starting_points % 2 == 0:
    bonus_points += 1
elif starting_points % 10 == 5:
    bonus_points += 2

print(bonus_points)
print(starting_points + bonus_points)



