presents = int(input())
n = int(input())
field = []
santa_position = []
good_kids = 0
good_kids_counter = 0
dirs = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}

for row in range(n):
    line = input().replace(' ', '')
    field.append(list(line))
    if 'S' in line:
        santa_position = [row, line.index('S')]
    if 'V' in line:
        for kid in line:
            if kid == 'V':
                good_kids += 1

command = input()
while presents > 0 and command != 'Christmas morning':
    position_changes = dirs[command]
    new_row = santa_position[0] + position_changes[0]
    new_col = santa_position[1] + position_changes[1]

    if field[new_row][new_col] == 'X' or field[new_row][new_col] == '-':
        field[santa_position[0]][santa_position[1]] = '-'
        field[new_row][new_col] = 'S'
        santa_position = [new_row, new_col]

    elif field[new_row][new_col] == 'V':
        field[santa_position[0]][santa_position[1]] = '-'
        field[new_row][new_col] = 'S'
        santa_position = [new_row, new_col]
        presents -= 1

    elif field[new_row][new_col] == 'C':
        field[santa_position[0]][santa_position[1]] = '-'
        field[new_row][new_col] = 'S'
        santa_position = [new_row, new_col]
        # up
        if 0 <= new_row -1 < n and 0 <= new_col < n:
            if field[santa_position[0] - 1][santa_position[1]] == 'X' or field[santa_position[0] - 1][santa_position[1]] == 'V':
                field[santa_position[0] - 1][santa_position[1]] = '-'
                presents -= 1
            if presents == 0:
                break
        # down
        if 0 <= new_row + 1 < n and 0 <= new_col < n:
            if field[santa_position[0] + 1][santa_position[1]] == 'X' or field[santa_position[0] + 1][santa_position[1]] == 'V':
                field[santa_position[0] + 1][santa_position[1]] = '-'
                presents -= 1
            if presents == 0:
                break
        # left
        if 0 <= new_row < n and 0 <= new_col - 1 < n:
            if field[santa_position[0]][santa_position[1] - 1] == 'X' or field[santa_position[0]][santa_position[1] - 1] == 'V':
                field[santa_position[0]][santa_position[1] - 1] = '-'
                presents -= 1
            if presents == 0:
                break
        # right
        if 0 <= new_row < n and 0 <= new_col + 1 < n:
            if field[santa_position[0]][santa_position[1] + 1] == 'X' or field[santa_position[0]][santa_position[1] + 1] == 'V':
                field[santa_position[0]][santa_position[1] + 1] = '-'
                presents -= 1
            if presents == 0:
                break

    command = input()

if not presents:
    print("Santa ran out of presents!")

for row in field:
    print(' '.join(row))

for row in field:
    for kid in row:
        if kid == 'V':
            good_kids_counter += 1
if good_kids_counter == 0:
    print(f"Good job, Santa! {good_kids} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_counter} nice kid/s.")