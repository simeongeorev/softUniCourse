rows, columns = [int(x) for x in input().split()]
abc = "abcdefghijklmnopqrstuvwxyz"

for i in range(rows):
    for j in range(columns):
        print(abc[i]+abc[i+j]+abc[i], end=" ")
    print()