rooms = int(input())
free_chairs = 0
game_on = True

for index in range(rooms):
    situation = input().split()
    chairs_left = len(situation[0]) - int(situation[1])
    if chairs_left >= 0:
        free_chairs += chairs_left
    else:
        print(f"{abs(chairs_left)} more chairs needed in room {index + 1}")
        game_on = False

if game_on: print(f"Game On, {free_chairs} free chairs left")
