num_sequence = list(map(int, input().split(", ")))

sorted_nums = list(sorted(num_sequence))

cycles = (sorted_nums[-1] - 1) // 10 + 1

for index in range(10, cycles * 10 + 10, 10):
    current_list = [num for num in num_sequence if num <= index]
    num_sequence = [num for num in num_sequence if num not in current_list]
    print(f"Group of {index}'s: {current_list}")
