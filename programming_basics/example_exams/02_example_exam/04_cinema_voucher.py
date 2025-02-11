# колко покупки от киното може да си купи Любо със спечеленият ваучер

voucher_money = int(input())

movie_tickets_count = 0
other_stuff_count = 0
movie_ticket_price = 0
other_stuff_price = 0

while True:
    command = input()
    if command == "End":
        print(f"{movie_tickets_count}")
        print(f"{other_stuff_count}")
        break

    if len(command) > 8:
        movie_ticket_price = ord(command[0]) + ord(command[1])
        if movie_ticket_price <= voucher_money:
            voucher_money -= movie_ticket_price
            movie_tickets_count += 1
        else:
            print(f"{movie_tickets_count}")
            print(f"{other_stuff_count}")
            break

    elif len(command) <= 8:
        other_stuff_price = ord(command[0])
        if other_stuff_price <= voucher_money:
            voucher_money -= other_stuff_price
            other_stuff_count += 1
        else:
            print(f"{movie_tickets_count}")
            print(f"{other_stuff_count}")
            break
