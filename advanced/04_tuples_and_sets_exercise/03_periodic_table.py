n = int(input())
chemicals = set()

for _ in range(n):
    input_chems = input().split()
    for chem in input_chems:
        chemicals.add(chem)

print(*chemicals, sep="\n")