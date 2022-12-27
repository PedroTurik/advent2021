with open('input1.txt') as f:
    a, b = f.readline().strip().split(',')
    X1, X2 = list(map(int, a.split('..')))
    Y1, Y2 = list(map(int, b.split('..')))

ans = set()

def is_target(x, y):
    return bool(X1 <= x <= X2 and Y1 <= y <= Y2)

def test_initial_speed(x, y):
    posx, posy = 0, 0
    vx, vy = x, y
    while posx <= X2 and posy >= Y1:
        posx += vx
        posy += vy
        if is_target(posx, posy): return True
        vy -= 1
        if vx < 0: vx += 1
        if vx > 0: vx -= 1
    return False

for x in range(1, X2 +1):
    for y in range(Y1-10, -Y1 + 10):
        if test_initial_speed(x, y):
            ans.add((x,y))

print(len(ans))



