n = int(input())
for _ in range(n):
    ranges = input().split("-")
    first_start, first_end = list(map(int, ranges[0].split(",")))
    second_start, second_end = list(map(int, ranges[1].split(",")))

    first_range = range(first_start, first_end+1)
    second_range = range(second_start, second_end+1)

    for
