n = 5
matrix = []
my_position = []
targets = []
directions_dict = {"right": (0, 1),
                   "left": (0, -1),
                   "up": (-1, 0),
                   "down": (1, 0)}
targets_hit = []

for row_i in range(n):
    matrix.append(input().split())

    for col_i in range(n):
        # get my position
        if matrix[row_i][col_i] == "A":
            my_position = [row_i, col_i]

        # get all targets positions
        elif matrix[row_i][col_i] == "x":
            targets.append([row_i, col_i])

n_commands = int(input())

for _ in range(n_commands):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == "move":
        steps = int(command[2])
        current_row, current_col = my_position
        desired_row = current_row + (directions_dict[direction][0] * steps)
        desired_col = current_col + (directions_dict[direction][1] * steps)

        if ([desired_row, desired_col] not in targets
                and desired_col in range(0, n)
                and desired_row in range(0, n)):
            my_position = [desired_row, desired_col]

    elif action == "shoot":
        bullet_position = my_position.copy()  # AI helped
        while True:
            desired_row = bullet_position[0] + directions_dict[direction][0]
            desired_col = bullet_position[1] + directions_dict[direction][1]

            # bullet is outside the matrix
            if desired_row not in range(0, n) or desired_col not in range(0, n):
                break

            # bullet hits target
            elif [desired_row, desired_col] in targets:
                targets_hit.append([desired_row, desired_col])
                targets.remove([desired_row, desired_col])
                matrix[desired_row][desired_col] = "."
                break

            # bullet doesn't hit target
            bullet_position = [desired_row, desired_col]

    if not targets:
        print(f"Training completed! All {len(targets_hit)} targets hit.")
        break
else:
    print(f"Training not completed! {len(targets)} targets left.")

print(*targets_hit, sep="\n")
