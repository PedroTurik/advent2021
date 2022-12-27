with open('input1.txt') as f:
    x, y = f.readline().strip().split(',')
    x1, x2 = list(map(int, x.split('..')))
    y1, y2 = list(map(int, y.split('..')))

print(x1,x2,y1,y2)


speed_at_zero = y1
height = 0

for i in range(0, -speed_at_zero):
    height += i

print(height)