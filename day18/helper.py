SPLIT_CHANGED = False

def add_left(n, idx, snail):
    start = None
    finish = None
    for i in range(idx, -1, -1):
        if snail[i].isdigit():
            if not start: start = i + 1
        elif start:
            finish = i + 1
            break
    if not start:
        return snail[:idx-1]
        
    return snail[:finish] + str(int(snail[finish:start]) + int(n)) + snail[start:idx-1]


def add_right(n, idx, snail):
    start = None
    finish = None
    for i in range(idx, len(snail)):
        if snail[i].isdigit():
            if not start:
                start = i
        elif start:
            finish = i
            break
    if not start:
        return snail[idx+1:]

    return snail[idx+1:start] + str(int(snail[start:finish]) + int(n)) + snail[finish:]

def explode(snail):
    snail = str(snail)
    snail.replace(' ', '')
    c_count = 0
    for i, c in enumerate(snail):
        if c_count == 5:
            close = 0
            for c in snail[i:]:
                if c == ']':
                    break
                close += 1
            a, b = snail[i:i + close].split(',')
            new_snail = eval((add_left(a, i, snail) + '0' + add_right(b, i+close, snail)).strip())
            break
        if c == '[': c_count += 1
        elif c == ']': c_count -= 1
    else:
        return False
    return new_snail


def splitter(snail):
    global SPLIT_CHANGED
    if not isinstance(snail, list) or SPLIT_CHANGED:
        return
    for i in [0, 1]:
        if type(snail[i]) == int and snail[i] > 9:
            snail[i] = [snail[i]//2, round(snail[i]/2)]
            SPLIT_CHANGED = True
            break
    else:
        splitter(snail[0])
        splitter(snail[1])

def clean(snail):
    new_snail = explode(snail)
    if new_snail:
        return new_snail
    else:
        splitter(snail)
    return (snail, SPLIT_CHANGED) if not new_snail else (new_snail, True)


def magnitude(snail):
    if type(snail) == int:
        return snail

    return 3*magnitude(snail[0]) + 2*magnitude(snail[1])
