def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

numbers_list = list(map(int, input().split()))

only_evens = list(filter(is_even, numbers_list))

print(only_evens)