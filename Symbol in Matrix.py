n = int(input())
matrix = [[x for x in input()] for _ in range(n)]
searched_symbol = input()
is_found = False
position = (0, 0)

for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched_symbol:
            position = (row, col)
            is_found = True
            break

if is_found:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")
