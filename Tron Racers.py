n = int(input())
field = []
f_position = []
s_position = []
game_over = False
dirs = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}

for row in range(n):
    line = list(input())
    field.append(line)
    if 'f' in line:
        f_position = [row, line.index('f')]
    if 's' in line:
        s_position = [row, line.index('s')]

while True:
    if game_over:
        break
    token = input().split()
    # first player
    f_direction = token[0]
    f_position_change = dirs[f_direction]
    f_new_row = f_position_change[0] + f_position[0]
    f_new_col = f_position_change[1] + f_position[1]

    # second_player
    s_direction = token[1]
    s_position_change = dirs[s_direction]
    s_new_row = s_position_change[0] + s_position[0]
    s_new_col = s_position_change[1] + s_position[1]

    if f_new_row < 0:
        f_new_row = n - 1
    if s_new_row < 0:
        s_new_row = n - 1
    if f_new_row >= n:
        f_new_row = 0
    if s_new_row >= n:
        s_new_row = 0
    if f_new_col < 0:
        f_new_col = n - 1
    if s_new_col < 0:
        s_new_col = n - 1
    if f_new_col >= n:
        f_new_col = 0
    if s_new_col >= n:
        s_new_col = 0

    # first player
    if field[f_new_row][f_new_col] == '*':
        field[f_position[0]][f_position[1]] = 'f'
        field[f_new_row][f_new_col] = 'f'
        f_position = [f_new_row, f_new_col]

    elif field[f_new_row][f_new_col] == 's':
        field[f_new_row][f_new_col] = 'x'
        game_over = True
        break

    # second player
    if 0 <= s_new_row < n and 0 <= s_new_col < n:
        if field[s_new_row][s_new_col] == '*':
            field[s_position[0]][s_position[1]] = 's'
            field[s_new_row][s_new_col] = 's'
            s_position = [s_new_row, s_new_col]

        elif field[s_new_row][s_new_col] == 'f':
            field[s_new_row][s_new_col] = 'x'
            game_over = True
            break

for row in field:
    print(''.join(row))
