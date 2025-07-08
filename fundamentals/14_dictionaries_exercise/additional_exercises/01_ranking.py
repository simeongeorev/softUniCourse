contests_dict = {}
users_dict = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    contests_dict[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break
    contest, password, username, points = command.split("=>")
    points = int(points)
    if contest not in contests_dict.keys() or contests_dict.get(contest) != password:
        continue

    if username not in users_dict.keys():
        users_dict[username] = {}

    if contest not in users_dict[username].keys():
        users_dict[username][contest] = points

    if points > users_dict[username][contest]:
        users_dict[username][contest] = points

best_user = ""
most_points = 0
for user, details_dict in users_dict.items():
    total_score = sum(details_dict.values())
    if total_score > most_points:
        most_points = total_score
        best_user = user

print(f"Best candidate is {best_user} with total {most_points} points.")
print("Ranking:")
sorted_users_dict = dict(sorted(users_dict.items()))
for user, info_dict in sorted_users_dict.items():
    sorted_info_dict = dict(sorted(info_dict.items(), key=lambda item: item[1], reverse=True))
    print(user)
    for contest, points in sorted_info_dict.items():
        print(f"#  {contest} -> {points}")
