number = int(input())

start_num = 1_111
end_num = 9_999
is_special_number = True

for divisor_num in range(start_num, end_num+1):

    for subdivisor_as_str in str(divisor_num):
        subdivisor_as_int = int(subdivisor_as_str)

        if subdivisor_as_int == 0:
            is_special_number = False
            continue

        elif number % subdivisor_as_int != 0:
            is_special_number = False

    if is_special_number:
        print(divisor_num, end=" ")

    is_special_number = True