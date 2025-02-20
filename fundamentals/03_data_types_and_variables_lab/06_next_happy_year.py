year = int(input())

while True:
    year+=1

    special = True

    year_string = str(year)

    # year_sorted = sorted(year_string)
    #
    # for i in range(len(year_sorted)-1):
    #     if year_sorted[i] == year_sorted[i+1]:
    #         special = False
    #         break
    #
    # if special:
    #     print(year)
    #     break

    new_string = ""

    for i in range(len(year_string)):
        new_string = year_string[i+1:]
        if year_string[i] in new_string:
            special = False
            break

    if special:
        print(year)
        break

