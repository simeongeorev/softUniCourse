from collections import deque

contestants = deque([int(x) for x in input().split()]) # FIFO
pies = [int(x) for x in input().split()]        # LIFO

while contestants and pies:
    current_contestant = contestants[0]
    current_pie = pies[-1]

    # contestant can eat the pie
    if current_contestant >= current_pie:

        current_contestant -= current_pie # subtract the pie pieces from the contestant's pie eating capacity
        pies.pop() # remove the pie from the last position

        contestants.popleft()
        if current_contestant > 0:
            contestants.append(current_contestant)



    elif current_pie > current_contestant:
        current_pie -= current_contestant
        contestants.popleft()

        if len(pies) > 1 and current_pie == 1:
            pies.pop()
            pies[-1] += current_pie
        else:
            pies[-1] = current_pie

if contestants and not pies:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join([str(x) for x in contestants])}")

elif not contestants and not pies:
    print("We have a champion!")

elif not contestants and pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join([str(x) for x in pies])}")




