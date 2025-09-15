from collections import deque

green_light_duration = int(input())
free_window_time = int(input())

cars_queue = deque()
cars_passed = 0

while (command := input()) != "END":
    if command == "green":
        green_seconds = green_light_duration
        yellow_seconds = free_window_time

        # 1st stage
        current_car = None
        current_car_length = None

        if cars_queue:
            current_car = cars_queue.popleft()
            current_car_length = deque(current_car)
        else:
            continue

        while green_seconds:
            if not current_car_length:
                if cars_queue:
                    current_car = cars_queue.popleft()
                    current_car_length = deque(current_car)
                else:
                    break
            green_seconds -= 1
            current_car_length.popleft()
            if not current_car_length:
                cars_passed += 1

        # 2nd stage
        if current_car_length:
            while yellow_seconds:
                if current_car_length:
                    yellow_seconds -= 1
                    current_car_length.popleft()
                    if not current_car_length:
                        cars_passed +=1
                        break
                else:
                    cars_passed += 1
                    break

            if current_car_length:
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car_length[0]}.")
                exit()

    else:
        cars_queue.append(command)

print("Everyone is safe.")
print(f"{cars_passed} total cars passed the crossroads.")