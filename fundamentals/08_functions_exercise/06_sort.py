def sort_nums(numbers: list):
    return list(sorted(numbers))

numbers = list(map(int, input().split()))

print(sort_nums(numbers))