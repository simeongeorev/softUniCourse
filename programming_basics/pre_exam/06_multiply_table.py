n = input()
number_1 = int(n[2])
number_2 = int(n[1])
number_3 = int(n[0])

for i in range(1, number_1 + 1):
    for j in range(1, number_2 + 1):
        for k in range(1, number_3 + 1):
            print(f"{i} * {j} * {k} = {i * j * k};")