rows, cols = [int(x) for x in input().split(', ')]
sum = 0
matrix = []

for row in range(rows):
    numbers = [int(x) for x in input().split(', ')]
    matrix.append(numbers)

for row in range(rows):
    for col in range(cols):
        sum += matrix[row][col]

print(sum)
print(matrix)