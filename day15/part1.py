from queue import PriorityQueue
from helper import Node, get_board


board = get_board()

Y = len(board) - 1
X = len(board[0]) - 1


heap = PriorityQueue()
visited = set()
heap.put(Node((0,0), 0, (Y,X)))


ans = None

while True:
    cur_node = heap.get()
    visited.add(cur_node.pos)
    if cur_node.pos == (Y, X):
        ans = cur_node.risk
        break
    y, x = cur_node.pos
    for y1, x1 in[(y+1, x),(y-1, x),(y, x+1), (y, x-1)]:
        if 0 <= y1 <= Y and 0 <= x1 <= X and (y1, x1) not in visited:
            heap.put(Node((y1, x1), cur_node.risk+board[y1][x1], (Y,X)))

print(ans)



