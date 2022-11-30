matrix = []
with open("input1.txt", "r") as f:
    for row in f.readlines():
        matrix.append([int(x) for x in row.strip()])

Y = len(matrix)
X = len(matrix[0])
counter = 0
size_list = []


def check_index(y, x):
    val = matrix[y][x]
    for yi, xi in [(y-1, x), (y+1, x), (y, x+1), (y, x-1)]:
        if 0 <= yi < len(matrix) and 0 <= xi < len(matrix[0]):
            if val >= matrix[yi][xi]:
                return False
    return True


def mark_basin(y, x):
    if matrix[y][x] != 9:
        matrix[y][x] = 9
        global counter
        counter += 1
        if y > 0: mark_basin(y-1, x)
        if y < Y-1: mark_basin(y+1, x)
        if x > 0: mark_basin(y, x-1)
        if x < X-1: mark_basin(y, x+1)


low_points = set()
for i in range(Y):
    for j in range(X):
        if check_index(i,j):
            low_points.add((i, j))


for y, x in low_points:
    mark_basin(y, x)
    size_list.append(counter)
    counter = 0


size_list.sort()
print(size_list[-1]*size_list[-2]*size_list[-3])