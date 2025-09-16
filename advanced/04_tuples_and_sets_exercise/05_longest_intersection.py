n = int(input())
longest_intersection = set()
for _ in range(n):
    ranges = input().split("-")
    first_start, first_end = list(map(int, ranges[0].split(",")))
    second_start, second_end = list(map(int, ranges[1].split(",")))

    first_range = range(first_start, first_end+1)
    second_range = range(second_start, second_end+1)

    first_set = set(i for i in first_range)
    second_set = set(i for i in second_range)

    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join(str(el) for el in longest_intersection)}] with length {len(longest_intersection)}")
