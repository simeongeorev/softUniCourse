number_of_visitors = int(input())

backs = 0
chests = 0
legses = 0
abses = 0
protein_shakes = 0
protein_bars = 0

for _ in range(number_of_visitors):
    activity = input()
    if activity == "Back":
        backs += 1
    elif activity == "Chest":
        chests += 1
    elif activity == "Legs":
        legses += 1
    elif activity == "Abs":
        abses += 1
    elif activity == "Protein shake":
        protein_shakes += 1
    elif activity == "Protein bar":
        protein_bars += 1

print(f"{backs} - back")
print(f"{chests} - chest")
print(f"{legses} - legs")
print(f"{abses} - abs")
print(f"{protein_shakes} - protein shake")
print(f"{protein_bars} - protein bar")
print(f"{(backs + chests + legses + abses) / number_of_visitors * 100:.2f}% - work out")
print(f"{(protein_shakes + protein_bars) / number_of_visitors * 100:.2f}% - protein")
