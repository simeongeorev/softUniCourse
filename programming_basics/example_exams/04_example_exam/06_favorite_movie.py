best_movie_name = ""
best_movie_points = 0

for _ in range(7):

    movie_name = input()

    if movie_name == "STOP":
        break

    movie_name_length = len(movie_name)

    ascii_points = 0

    for c in movie_name:

        ascii_points += ord(c)

        if c.isupper(): # cap letter
            ascii_points -= movie_name_length

        elif c.islower(): # non-cap letter
            ascii_points -= movie_name_length * 2

    if ascii_points > best_movie_points:
        best_movie_name = movie_name
        best_movie_points = ascii_points
else:
    print("The limit is reached.")

print(f"The best movie for you is {best_movie_name} with {best_movie_points} ASCII sum.")

