class MatrixSizeError(Exception):
    pass


class MatrixContentError(Exception):
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()


mtrx = []

while True:
    line = input().split()

    if not line:
        break
    mtrx.append(line)


for row in mtrx:
    # validate if the matrix size is NxN
    if len(row) != len(mtrx):
        raise MatrixSizeError("The size of the matrix is not a perfect square")

    # validate if all matrix elements are integers
    if not all(str(el).isnumeric() for el in row):
        raise MatrixContentError("The matrix must consist of only integers")

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')
