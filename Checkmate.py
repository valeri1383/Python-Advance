board = []
queen_position = []
king_position = []
list_queens = []
for row in range(8 + 1):
    line = list(input().split())
    board.append(line)
    for el in line:
        if el == 'Q':
            queen_position = [row, line.index(el)]
            queen_row = queen_position[0]
            queen_col = queen_position[1]
            list_queens.append(queen_position)


while queen_row < 8:

    queen_row += 1
    #if board[2][0] == '.':
        #print('Bravo')








for row in board:
    print(' '.join(row))