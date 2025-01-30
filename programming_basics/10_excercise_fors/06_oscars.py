# Точките, които актьора получава се формират от
# дължината на името на оценяващия умножено по точките, които дава делено на две.

# Ако резултатът в някой момент надхвърли 1250.5
# програмата трябва да прекъсне и да се отпечата, че дадения актьор е получил номинация.

actor_name = str(input())
academy_points = float(input())
scorers_count = int(input())

points_from_scorer_name = 0
total_points = academy_points
POINT_LIMIT = 1250.5

for i in range(0, scorers_count):
    scorer_name = str(input())
    scorer_points = float(input())
    points_from_scorer_name = len(scorer_name) * scorer_points / 2
    total_points += points_from_scorer_name
    if total_points > POINT_LIMIT:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        exit()

print(f"Sorry, {actor_name} you need {POINT_LIMIT - total_points:.1f} more!")



