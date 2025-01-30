import math

number_of_tourneys = int(input())
starting_points = int(input())

points_from_tourneys = 0

tourneys_won = 0

for tourney_number in range(0, number_of_tourneys):

    status_in_tourney = str(input())

    if status_in_tourney == "W":
        points_from_tourneys += 2000
        tourneys_won += 1

    if status_in_tourney == "F":
        points_from_tourneys += 1200

    if status_in_tourney == "SF":
        points_from_tourneys += 720

final_points = starting_points + points_from_tourneys
middle_points = points_from_tourneys / number_of_tourneys
percent_of_tourneys_won = tourneys_won / number_of_tourneys * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(middle_points)}")
print(f"{percent_of_tourneys_won:.2f}%")

