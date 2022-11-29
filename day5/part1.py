matrix = [[0 for _ in range(1000)] for _ in range(1000)]


def read():
    clouds=[]
    for x in open('input1.txt', 'r').readlines():
        points = x.split(" -> ")
        x1,y1 = points[0].split(',')
        x2,y2 = points[1].split(',')
        clouds.append(((int(x1),int(y1)), (int(x2),int(y2))))
    return tuple(clouds)

clouds = read()

for cloud in clouds:
    (x1,y1), (x2,y2) = cloud
    if x1 == x2:
        if y1 > y2: 
            y1, y2 = y2, y1
        for i in range(y1, y2+1):
            matrix[i][x1] += 1
    elif y1 == y2:
        if x1 > x2: 
            x1, x2 = x2, x1
        for i in range(x1, x2+1):
            matrix[y1][i] += 1

counter = 0
for row in matrix:
    for col in row:
        if col > 1:
            counter += 1

print(counter)

