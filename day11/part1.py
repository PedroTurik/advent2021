matrix = []
with open("input1.txt", "r") as f:
    for row in f.readlines():
        matrix.append([int(x) for x in row.strip()])
Y = len(matrix)
X = len(matrix[0])
flashed = set()

counter = 0

def clean_up():
    flashed.clear()
    for i in range(Y):
        for j in range(X):
            if matrix[i][j] > 9:
                matrix[i][j] = 0

def blink(y, x):
    for i in [y-1, y, y+1]:
        for j in [x-1, x, x+1]:
            if i == y and j == x:
                continue
            if 0 <= i < Y and 0 <= j < X:
                matrix[i][j] += 1
                if matrix[i][j] > 9 and (i,j) not in flashed:
                    global counter 
                    counter += 1
                    flashed.add((i,j))
                    blink(i,j)
            



def step(y, x):
    matrix[y][x] += 1
    if matrix[y][x] > 9 and (y,x) not in flashed:
        global counter 
        counter += 1
        flashed.add((y,x))
        blink(y, x)


for _ in range(100):
    for i in range(Y):
        for j in range(X):
            step(i, j)
    clean_up()


print(counter)