def round_numbers(numbers: list) -> list:
    for i in range(len(numbers)):
        numbers[i] = round(float(numbers[i]))
    return numbers

print(round_numbers(input().split()))