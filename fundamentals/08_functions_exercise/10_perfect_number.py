def is_perfect_num(number: int):
    right_dividers = []
    for i in range(1, number):
        if number % i == 0:
            right_dividers.append(i)
    if sum(right_dividers) == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

is_perfect_num(int(input()))