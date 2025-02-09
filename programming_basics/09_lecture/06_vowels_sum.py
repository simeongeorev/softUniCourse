sequence = str(input())

sum = 0

for i in range(0, len(sequence)):
    if sequence[i] == "a":
        sum += 1
    elif sequence[i] == "e":
        sum += 2
    elif sequence[i] == "i":
        sum += 3
    elif sequence[i] == "o":
        sum += 4
    elif sequence[i] == "u":
        sum += 5

print(sum)
