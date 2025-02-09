interval_start = int(input())
interval_end = int(input())
magick_number = int(input())

counter = 0
combination_found = False

for first_num_conf in range(interval_start, interval_end + 1):
    for second_num_conf in range(interval_start, interval_end + 1):
        counter += 1
        if first_num_conf + second_num_conf == magick_number:
            print(f"Combination N:{counter} ({first_num_conf} + {second_num_conf} = {magick_number})")
            combination_found = True
            break
        else:
            continue
    if combination_found: break
else:
    print(f"{counter} combinations - neither equals {magick_number}")
