from collections import defaultdict
from copy import deepcopy

conections = defaultdict(set)
with open('input1.txt') as f:
    for row in f.readlines():
        k, v = row.strip().split("-")
        conections[k].add(v)
        conections[v].add(k)

counter = 0

def dive(dic, node, ban_set, special=None, passed_special=False):
    if node == special:
        passed_special = True


    if node == 'end':
        if not special or (special and passed_special):
            global counter
            counter += 1
    elif node not in ban_set:
        cur = dic.get(node, False)

        if cur and not special and node != 'start':
            for n in cur:
                if n != 'start':
                    dive(deepcopy(dic), n, deepcopy(ban_set), node, passed_special)

        if node[0].islower():
            ban_set.add(node)

        if cur:
            for n in cur:
                if n != 'start':
                    dive(deepcopy(dic), n, deepcopy(ban_set), special, passed_special)


dive(conections, 'start', set(), None, False)

print(counter)