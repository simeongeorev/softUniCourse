import itertools

def possible_permutations(input_list: list):
    for item in itertools.permutations(input_list):
        yield list(item)

[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
