def has_won(board):
    for row in board:
        if all([x=='#' for x in row]):
            return True
    
    for i in range(5):
        count = 0
        for row in board:
            if row[i] != '#':
                count += 1
        if not count:
            return True
    return False

def pontuation(board, draw):
    ret = 0
    for row in board:
        for col in row:
            if type(col) == int:
                ret += col
    return ret*draw




with open('input2.txt') as f:
    draws = [int(x) for x in f.readline().split(',')]
    _ = f.readline()
    raw_boards = f.readlines()

boards = []
cur_board = []
for row in raw_boards:
    if row == '\n': 
        boards.append(cur_board)
        cur_board = []
        continue
    
    cur_board.append([int(n) for n in row.strip().split()])

def play():
    finished_boards = []
    boards_left = len(boards)
    for draw in draws:
        for board in boards:
            if board in finished_boards: continue
            for i, row in enumerate(board):
                for j, col in enumerate(row):
                    if col == draw:
                        board[i][j] = '#'

            if has_won(board):
                boards_left -= 1
                finished_boards.append(board)
                if not boards_left:
                    return pontuation(board, draw)

print(play())
              