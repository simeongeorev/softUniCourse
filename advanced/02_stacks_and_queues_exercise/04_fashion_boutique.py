clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks_used = 1
current_pile = 0

while clothes:
    current_clothe = clothes.pop()
    current_pile += current_clothe
    if current_pile > rack_capacity:
        current_pile = current_clothe
        racks_used += 1
    elif current_pile == rack_capacity and clothes:
        current_pile = 0
        racks_used += 1

print(racks_used)

