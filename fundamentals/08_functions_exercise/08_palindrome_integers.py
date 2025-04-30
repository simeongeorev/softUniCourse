def is_palindrome(input_str: str):
    numbers = input_str.split(", ")

    for i in range(len(numbers)):
        numbers[i] = list(numbers[i])

        backwards_list = []

        for y in range(len(numbers[i]) - 1, -1, -1):
            backwards_list.append(numbers[i][y])

        if numbers[i] == backwards_list:
            print(True)
        else:
            print(False)

is_palindrome(input())
