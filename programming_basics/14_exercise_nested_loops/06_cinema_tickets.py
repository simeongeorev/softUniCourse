movie_name = input()
total_tickets_counter = 0

student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie_name != "Finish":
    empty_seats = int(input())
    full_room_counter = 0

    for _ in range(empty_seats):
        type_of_ticket = input()

        if type_of_ticket == "End":
            break

        elif type_of_ticket == "student":
            student_tickets += 1

        elif type_of_ticket == "standard":
            standard_tickets += 1

        elif type_of_ticket == "kid":
            kid_tickets += 1

        full_room_counter += 1
        total_tickets_counter += 1

    print(f"{movie_name} - {(full_room_counter / empty_seats * 100):.2f}% full.")
    movie_name = input()

if movie_name == "Finish":
    print(f"Total tickets: {total_tickets_counter}")
    print(f"{(student_tickets / total_tickets_counter * 100):.2f}% student tickets.")
    print(f"{(standard_tickets / total_tickets_counter * 100):.2f}% standard tickets.")
    print(f"{(kid_tickets / total_tickets_counter * 100):.2f}% kids tickets.")