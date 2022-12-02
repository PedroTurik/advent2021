class Node:
    def __init__(self, pos, risk, target) -> None:
        self.pos = pos
        self.risk = risk
        self.manhatan = (target[0]-pos[0]) + (target[1]-pos[1])    
    def __lt__(self, other) -> bool:
        return self.risk + (self.manhatan) < other.risk + (other.manhatan)

    def __gt__(self, other) -> bool:
        return self.risk + (self.manhatan) > other.risk + (other.manhatan)
    
    def __repr__(self) -> str:
        return f"{self.pos},  {self.risk}"


def get_board():
    board = []
    with open('input1.txt') as f:
        for row in f.readlines():
            tmp = []
            for n in row.strip():
                tmp.append(int(n))
            board.append(tmp)
    return board


def multiply_board(board, factor):
    Y = len(board)
    X = len(board[0])
    rows, cols = Y*factor, X
    new_matrix = [([0]*cols) for _ in range(rows)]

    for i, row in enumerate(board):
        for j, n in enumerate(row):
            for f in range(factor):
                new_matrix[i+f*Y][j] = ((n+f) if n+f < 10 else (n+f)%10+1)
    
    for row in new_matrix:
        for n in row:
            if n == 9:
                row.append(1)
            else:
                row.append(n+1)
            if len(row) == X*factor:
                break

    return new_matrix


