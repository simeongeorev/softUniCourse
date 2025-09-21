rows = int(input())
matrix = []
even_matrix = []
for _ in range(rows):
    input_list = list(map(int, input().split(", ")))
    matrix.append(input_list)

even_matrix = [[x for x in el if x % 2 == 0] for el in matrix]

print(even_matrix)