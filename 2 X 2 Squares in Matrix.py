rows, cols = [int(x) for x in input().split(' ')]
matrix = [[x for x in input().split(' ')] for _ in range(rows)]
count_matches = 0

def current_submatrix(matrix, row, col):
    return matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]


for row in range(rows - 1):
    for col in range(cols - 1):
        if current_submatrix(matrix, row, col):
            count_matches += 1

print(count_matches)