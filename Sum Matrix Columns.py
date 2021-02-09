row, colon = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(' ')] for _ in range(row)]

# for i in range(colon):
#     result = 0
#     for j in range(row):
#         result += matrix[j][i]
#     print(result)

for col in zip(*matrix):
    print(sum(col))
