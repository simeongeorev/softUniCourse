SPACESHIP_S = "S"
METEORITE_S = "M"
PLANET_B_S = "P"
SPACE_STATION_S = "R"
EMPTY_SPACE = "."

N = int(input())
matrix = []

current_position = None
planet_b_position = None
resources = 100

for row_i in range(N):
    matrix.append(input().split())

    if SPACESHIP_S in matrix[row_i]:
        current_position = [row_i, matrix[row_i].index(SPACESHIP_S)]
    if PLANET_B_S in matrix[row_i]:
        planet_b_position = [row_i, matrix[row_i].index(PLANET_B_S)]

movements_dict = {"right": [0, 1],
                  "left": [0, -1],
                  "up": [-1, 0],
                  "down": [1, 0]}

while resources >= 5:
    # lower the resources
    resources -= 5

    command = input()
    cur_row, cur_col = current_position
    current_position_symbol = matrix[cur_row][cur_col]
    new_row, new_col = cur_row + movements_dict[command][0], cur_col + movements_dict[command][1]

    # if the ship is outside the borders
    if (new_row < 0 or new_row >= N) or (new_col < 0 or new_col >= N):
        print("Mission failed! The spaceship was lost in space.")
        break

    new_position = [new_row, new_col]
    new_position_symbol = matrix[new_row][new_col]

    # successfully arrives to Planet B!
    if new_position == planet_b_position:
        if current_position_symbol != SPACE_STATION_S:
            matrix[cur_row][cur_col] = EMPTY_SPACE
        print(f"Mission accomplished!"
              f" The spaceship reached Planet B with {resources} resources left.")
        break

    # hitting a meteorite
    elif new_position_symbol == METEORITE_S:
        resources -= 5
        if current_position_symbol != SPACE_STATION_S:
            matrix[cur_row][cur_col] = EMPTY_SPACE
        matrix[new_row][new_col] = SPACESHIP_S
        current_position = new_position

    # arriving at a space station
    elif new_position_symbol == SPACE_STATION_S:
        resources += 10
        if resources > 100:
            resources = 100
        if current_position_symbol != SPACE_STATION_S:
            matrix[cur_row][cur_col] = EMPTY_SPACE
        current_position = new_position

    # arriving at an empty space
    elif new_position_symbol == EMPTY_SPACE:
        if current_position_symbol != SPACE_STATION_S:
            matrix[cur_row][cur_col] = EMPTY_SPACE
        matrix[new_row][new_col] = SPACESHIP_S
        current_position = new_position
else:
    print("Mission failed! The spaceship was stranded in space.")

for row in matrix:
    print(" ".join(row))