input_str = input().split("|")
matrix = [[y for y in input_str[i].split()] for i in range(len(input_str) - 1, -1, -1)]
print(" ".join([num for row in matrix for num in row]))