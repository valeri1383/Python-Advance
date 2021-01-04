n = int(input())
field = []
snake_position = []
first_burrow_position = [0, 0]
second_burrow_position = [0, 0]
food = 0
inside = True
dirs = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}

for row in range(n):
    line = list(input())
    field.append(line)
    if 'S' in line:
        snake_position = [row, line.index('S')]
    if 'B' in line and first_burrow_position == [0, 0]:
        first_burrow_position = [row, line.index('B')]
    elif 'B' in line and second_burrow_position == [0, 0]:
        second_burrow_position = [row, line.index('B')]

while food < 10 and inside:
    command = input()
    position_changes = dirs[command]
    new_row = snake_position[0] + position_changes[0]
    new_col = snake_position[1] + position_changes[1]
    if 0 <= new_row < n and 0 <= new_col < n:
        if field[new_row][new_col] == '-':
            field[snake_position[0]][snake_position[1]] = '.'
            field[new_row][new_col] = 'S'
            snake_position = [new_row, new_col]

        elif field[new_row][new_col] == '*':
            food += 1
            field[snake_position[0]][snake_position[1]] = '.'
            field[new_row][new_col] = 'S'
            snake_position = [new_row, new_col]

        elif field[new_row][new_col] == 'B':
            if [new_row, new_col] == first_burrow_position:
                field[snake_position[0]][snake_position[1]] = '.'
                field[new_row][new_col] = '.'
                field[second_burrow_position[0]][second_burrow_position[1]] = 'S'
                snake_position = [second_burrow_position[0], second_burrow_position[1]]

            elif [new_row, new_col] == second_burrow_position:
                field[snake_position[0]][snake_position[1]] = '.'
                field[first_burrow_position[0]][first_burrow_position[1]] = 'S'
                snake_position = [first_burrow_position[0], first_burrow_position[1]]

    else:
        field[snake_position[0]][snake_position[1]] = '.'
        inside = False

if not inside:
    print('Game over!')
if food >= 10:
    print(f'You won! You fed the snake.')
print(f'Food eaten: {food}')
for row in field:
    print(f''.join(row))