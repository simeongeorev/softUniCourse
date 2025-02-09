floors = int(input())
apartments = int(input())
counter = 0

for floor in range(floors, 0, -1):
    counter += 1
    for apartment in range(apartments):
        if counter == 1:
            print(f"L{floor}{apartment}", end=' ')
        elif floor % 2 == 0:
            print(f"O{floor}{apartment}", end=' ')
        else:
            print(f"A{floor}{apartment}", end=' ')
    print()

