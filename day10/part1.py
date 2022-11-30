with open("input1.txt") as f:
    rows = [x.strip() for x in f.readlines()]

openers = {'(', '[','<', '{'}
closers = {
    ')':'(',
    ']':'[',
    '>':'<', 
    '}':'{'
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

ans = 0

for row in rows:
    stack = []
    for col in row:
        if col in openers: 
            stack.append(col)
        else:
            if stack[-1] == closers[col]:
                stack.pop()
            else:
                ans += points[col]
                break

print(ans)