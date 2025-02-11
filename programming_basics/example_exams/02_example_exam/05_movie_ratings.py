n_movies = int(input())

highest_rated_film_name = ""
highest_rated_film_score = 0
lowest_rated_film_name = ""
lowest_rated_film_score = 11
total_rating = 0

for i in range(n_movies):

    film_name = input()
    film_rating = float(input())

    if film_rating > highest_rated_film_score:
        highest_rated_film_score = film_rating
        highest_rated_film_name = film_name

    if film_rating < lowest_rated_film_score:
        lowest_rated_film_score = film_rating
        lowest_rated_film_name = film_name

    total_rating += film_rating

average_rating = total_rating / n_movies

print(f"{highest_rated_film_name} is with highest rating: {highest_rated_film_score:.1f}")
print(f"{lowest_rated_film_name} is with lowest rating: {lowest_rated_film_score:.1f}")
print(f"Average rating: {average_rating:.1f}")



