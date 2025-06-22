target_values = list(map(int, input().split()))
shot_targets_indexes = []

while True:

    command = input()

    if command == "End":
        break

    else:
        index_to_shoot = int(command)

        if index_to_shoot not in range(len(target_values)):
            continue

        shot_target_value = target_values[index_to_shoot]

        if index_to_shoot not in shot_targets_indexes:
            target_values[index_to_shoot] = -1
        else:
            continue

        shot_targets_indexes.append(index_to_shoot)

        for i in range(len(target_values)):
            if target_values[i] == -1:
                continue

            elif target_values[i] > shot_target_value:
                target_values[i] -= shot_target_value

            elif target_values[i] <= shot_target_value:
                target_values[i] += shot_target_value

print(f"Shot targets: {len(shot_targets_indexes)} ->", end=" ")
for target in target_values:
    print(target, end= " ")



