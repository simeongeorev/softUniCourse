initial_energy = 100
initial_coins = 100

events_list = input().split("|")

handled_everything = True

for event in events_list:
    event_as_list = event.split("-")
    event_or_ingredient = event_as_list[0]
    event_value = int(event_as_list[1])

    if event_or_ingredient == "rest":
        if initial_energy + event_value <= 100:
            initial_energy += event_value
            print(f"You gained {event_value} energy.")
        else:
            print(f"You gained {100 - initial_energy} energy.")
            initial_energy = 100

        print(f"Current energy: {initial_energy}.")

    elif event_or_ingredient == "order":
        if initial_energy >= 30:
            initial_coins += event_value
            initial_energy -= 30
            print(f"You earned {event_value} coins.")
        else:
            initial_energy += 50
            if initial_energy > 100:
                initial_energy = 100
            print("You had to rest!")

    else:
        if initial_coins >= event_value:
            initial_coins -= event_value
            print(f"You bought {event_or_ingredient}.")
        else:
            handled_everything = False
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            break

if handled_everything:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
