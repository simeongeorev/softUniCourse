from collections import deque

cups = deque(map(int, input().split())) # start from the first
bottles = list(map(int, input().split())) # start from the last

wasted_water = 0
filled_cups = 0

while cups and bottles:
    current_bottle = bottles.pop() # gets last bottle
    current_cup = cups[0]
    if current_bottle >= current_cup: # cup gets filled
        current_cup = cups.popleft()
        filled_cups += 1
        wasted_water += current_bottle - current_cup
    elif current_bottle < current_cup: # cup needs more water
        cups[0] -= current_bottle

# final prints
if bottles:
    bottles.reverse()
    print(f"Bottles: {' '.join([str(bottle) for bottle in bottles])}")
elif cups:
    print(f"Cups: {' '.join([str(cup) for cup in cups])}")
print(f"Wasted litters of water: {wasted_water}")
