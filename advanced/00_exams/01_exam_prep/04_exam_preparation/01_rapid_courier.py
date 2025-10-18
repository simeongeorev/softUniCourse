from collections import deque

packages_weights = [int(x) for x in input().split()] # last
couriers_capacities = deque([int(x) for x in input().split()]) # first

total_weight = 0

while packages_weights and couriers_capacities:
    cur_package = packages_weights.pop()
    cur_courier = couriers_capacities.popleft()

    # can deliver the package
    if cur_courier >= cur_package:
        if cur_courier > cur_package:
            cur_courier -= 2 * cur_package
            if cur_courier > 0:
                couriers_capacities.append(cur_courier)
        total_weight += cur_package

    # cannot deliver the package
    else:
        cur_package -= cur_courier
        packages_weights.append(cur_package)
        total_weight += cur_courier

print(f"Total weight: {total_weight} kg")

if not couriers_capacities and not packages_weights:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif not couriers_capacities:
    print(f"Unfortunately, there are no more available couriers to deliver the"
          f" following packages: {', '.join(str(x) for x in packages_weights)}")
elif not packages_weights:
    print(f"Couriers are still on duty:"
          f" {', '.join(str(x) for x in couriers_capacities)}"
          f" but there are no more packages to deliver.")


