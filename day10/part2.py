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
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

ans = []
for row in rows:
    stack = []
    for col in row:
        if col in openers: 
            stack.append(col)
        else:
            if stack[-1] == closers[col]:
                stack.pop()
            else:
                break
    else:
        cur = 0
        for v in reversed(stack):
            cur *= 5
            cur += points[v]
        ans.append(cur)


ans.sort()

print(ans[len(ans)//2])