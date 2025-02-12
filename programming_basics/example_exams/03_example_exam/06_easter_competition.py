n_kozunaci = int(input())

highest_rated_chef = ""
highest_rating_points = 0

for _ in range(n_kozunaci):

    baker_name = input() # izrejdame shefovete

    current_points_total = 0

    while True:

        command = input()

        if command == "Stop":
            break
        else:
            rating = int(command)
            current_points_total += rating

    print(f"{baker_name} has {current_points_total} points.")

    if current_points_total > highest_rating_points: # namirame top shefa
        highest_rating_points = current_points_total
        highest_rated_chef = baker_name
        print(f"{highest_rated_chef} is the new number 1!")

print(f"{highest_rated_chef} won competition with {highest_rating_points} points!")