text = input()
n = int(input())
field = []
player_position = []
dirs = {'up': [-1, 0], 'down': [1, 0], 'right': [0, 1], 'left': [0, -1]}

for row in range(n):
    line = list(input())
    if 'P' in line:
        player_position = [row, line.index('P')]
    field.append(line)

command = input()
while command != 'end':
    direction_change = dirs[command]
    next_row = player_position[0] + direction_change[0]
    next_col = player_position[1] + direction_change[1]
    next_position = [next_row, next_col]
    if 0 <= next_row < n and 0 <= next_col < n:
        if field[next_row][next_col] == '-':
            field[player_position[0]][player_position[1]] = '-'
            player_position = next_position
            field[player_position[0]][player_position[1]] = 'P'
        else:
            field[player_position[0]][player_position[1]] = '-'
            text += field[next_row][next_col]
            player_position = next_position
            field[player_position[0]][player_position[1]] = 'P'

    else:
        text = text[:-1]

    command = input()

print(text)
for i in range(n):
    print(''.join(field[i]))