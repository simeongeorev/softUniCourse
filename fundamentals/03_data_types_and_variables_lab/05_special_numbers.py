n = int(input())
n_as_string = str(n)
number_of_digits = len(n_as_string)

for i in range(1, n + 1):

    special_number = False
    number = 0

    for j in range(len(str(i))):
        number += int(str(i)[j])

    if number == 5 or number == 7 or number == 11:
        special_number = True

    print(f"{i} -> {special_number}")
