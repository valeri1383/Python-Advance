n = int(input())
count_commands = int(input())
square = []
player_position = []
dirs = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
win = False

for row in range(n):
    line = list(input())
    if 'f' in line:
        player_position = [row, line.index('f')]
    square.append(line)

for _ in range(count_commands):
    command = input()
    position_change = dirs[command]
    new_row = player_position[0] + position_change[0]
    new_col = player_position[1] + position_change[1]

    # inside
    if 0 <= new_row < n and 0 <= new_col < n:
        if square[new_row][new_col] == '-':
            square[player_position[0]][player_position[1]] = '-'
            square[new_row][new_col] = 'f'
            player_position = [new_row, new_col]

        elif square[new_row][new_col] == 'B':
            square[player_position[0]][player_position[1]] = '-'
            if command == 'up':
                new_row = player_position[0] + position_change[0] - 1
                square[new_row][new_col] = 'f'
                player_position = [new_row, new_col]
            elif command == 'down':
                new_row = player_position[0] + position_change[0] + 1
                square[new_row][new_col] = 'f'
                player_position = [new_row, new_col]
            elif command == 'left':
                new_col = player_position[1] + position_change[1] - 1
                square[new_row][new_col] = 'f'
                player_position = [new_row, new_col]
            elif command == 'right':
                new_col = player_position[1] + position_change[1] + 1
                square[new_row][new_col] = 'f'
                player_position = [new_row, new_col]

        elif square[new_row][new_col] == 'T':
            square[player_position[0]][player_position[1]] = 'f'
            player_position = [player_position[0], player_position[1]]

        elif square[new_row][new_col] == 'F':
            square[player_position[0]][player_position[1]] = '-'
            square[new_row][new_col] = 'f'
            player_position = [new_row, new_col]
            win = True
            break

    # outside
    else:
        if new_row < 0 or new_row >= n:
            if new_row < 0:
                new_row = n - 1
            elif new_row >= n:
                new_row = 0
            square[player_position[0]][player_position[1]] = '-'
            if square[new_row][new_col] == 'F':
                square[new_row][new_col] = 'f'
                player_position = [new_row, new_col]
                win = True
                break
            else:
                square[new_row][new_col] = 'f'
                player_position = [new_row, new_col]
        elif new_col < 0 or new_col >= n:
            if new_col < 0:
                new_col = n - 1
            elif new_col >= n:
                new_col = 0
            square[player_position[0]][player_position[1]] = '-'
            if square[new_row][new_col] == 'F':
                square[new_row][new_col] = 'f'
                player_position = [new_row, new_col]
                win = True
                break
            else:
                square[new_row][new_col] = 'f'
                player_position = [new_row, new_col]


if win:
    print(f'Player won!')
else:
    print('Player lost!')
for row in square:
    print(''.join(row))