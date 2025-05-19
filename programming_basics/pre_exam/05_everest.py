meters_climbed_total = 5_364
EVEREST = 8_848
days_passed = 1

while True:
    command = input()

    if command == "END":
        print("Failed!")
        print(meters_climbed_total)
        break

    if command == "Yes":
        days_passed += 1

    meters_climbed = int(input())

    if days_passed > 5:
        print("Failed!")
        print(meters_climbed_total)
        break

    meters_climbed_total += meters_climbed

    if meters_climbed_total >= EVEREST:
        print(f"Goal reached for {days_passed} days!")
        break


