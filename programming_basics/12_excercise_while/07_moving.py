free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

space_total = free_space_width * free_space_length * free_space_height

space_taken = 0

command = input()
while command != "Done":
    space_taken += int(command)

    if space_total - space_taken <= 0:
        print(f"No more free space! You need {space_taken - space_total} Cubic meters more.")
        break

    command = input()
else:
    print(f"{space_total - space_taken} Cubic meters left.")