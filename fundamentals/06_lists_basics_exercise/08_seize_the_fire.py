fire_list = input().split("#")

amount_of_water = int(input())

high_fire_range = range(81, 126)
medium_fire_range = range(51, 81)
low_fire_range = range(1, 51)

effort = 0
fires_taken_out = []

for fire_cell in fire_list:
    fire_info_list = fire_cell.split(" = ")
    fire_type = fire_info_list[0]
    fire_range_current = int(fire_info_list[1])

    if ((fire_type == "High" and fire_range_current in high_fire_range)
            or (fire_type == "Medium" and fire_range_current in medium_fire_range)
            or (fire_type == "Low" and fire_range_current in low_fire_range)):
        if fire_range_current > amount_of_water:
            continue
        else:
            amount_of_water -= fire_range_current
            effort += fire_range_current * 0.25
            fires_taken_out.append(fire_range_current)

print("Cells:")
for fire in fires_taken_out:
    print(" -", fire)
print(f"Effort: {effort:.2f}")
print("Total Fire:", sum(fires_taken_out))
