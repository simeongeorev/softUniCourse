from collections import deque

bullet_price = int(input()) # can be 0
gun_barrel_size = int(input())
bullets = list(map(int, input().split())) # shooting back to front
locks = deque(map(int, input().split())) # front to back
value_of_intelligence = int(input())
bullets_fired = 0

while bullets and locks:
    current_bullet = bullets.pop() # shoots bullet
    bullets_fired += 1

    if current_bullet <= locks[0]: # valid bullet - lock breaks
        locks.popleft() # lock broken
        print("Bang!")
    elif current_bullet > locks[0]: # invalid bullet - lock stays
        print("Ping!")

    if bullets_fired % gun_barrel_size == 0 and bullets_fired != 0: # check if it's time for reload
        if bullets: # check if there are any bullets left
            print("Reloading!")

# final prints
if bullets:
    money_earned = value_of_intelligence - bullets_fired * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${money_earned}" )
elif locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = value_of_intelligence - bullets_fired * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${money_earned}" )