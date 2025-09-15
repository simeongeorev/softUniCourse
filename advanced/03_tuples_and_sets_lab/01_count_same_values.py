numbers = tuple(map(float, input().split()))
number_occurrence = {}

for number in numbers:
    if number not in number_occurrence.keys():
        number_occurrence[number] = 0
    number_occurrence[number] += 1

for number, occurrences in number_occurrence.items():
    print(f"{number:.1f} - {occurrences} times")