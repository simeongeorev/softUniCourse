command_input = input()
STEPS_GOAL = 10000
total_steps = 0

while command_input != "Going home":
    steps = int(command_input)
    total_steps += steps
    if total_steps >= STEPS_GOAL:
        print("Goal reached! Good job!")
        print(f"{total_steps - STEPS_GOAL} steps over the goal!")
        break
    command_input = input()

else:
    steps_to_home = int(input())
    total_steps += steps_to_home
    if total_steps >= STEPS_GOAL:
        print("Goal reached! Good job!")
        print(f"{total_steps - STEPS_GOAL} steps over the goal!")
    else:
        print(f"{STEPS_GOAL - total_steps} more steps to reach goal.")

