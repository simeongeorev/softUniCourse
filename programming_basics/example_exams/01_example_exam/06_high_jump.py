from tokenize import endpats

height_target = int(input())
current_target = height_target - 30
unsuccessful_attempts = 0
attempts = 0
while True:
    jump_height = int(input())

    attempts += 1

    if jump_height > current_target:
        unsuccessful_attempts = 0

    elif jump_height <= current_target:
        unsuccessful_attempts += 1
        if unsuccessful_attempts == 3:
            print(f"Tihomir failed at {current_target}cm "
                  f"after {attempts} jumps.")
            break
        continue

    if jump_height > height_target and current_target == height_target:
        print(f"Tihomir succeeded, he jumped over {height_target}cm"
              f" after {attempts} jumps.")
        break

    current_target += 5
