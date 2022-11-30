matrix = []
with open("input1.txt", "r") as f:
    for row in f.readlines():
        matrix.append([int(x) for x in row.strip()])


def check_index(y, x):
    val = matrix[y][x]
    for yi, xi in [(y-1, x), (y+1, x), (y, x+1), (y, x-1)]:
        if 0 <= yi < len(matrix) and 0 <= xi < len(matrix[0]):
            if val >= matrix[yi][xi]:
                return 0
    return val + 1
    




ans = 0
for i, y in enumerate(matrix):
    for j, x in enumerate(y):
        ans += check_index(i, j)

print(ans)
