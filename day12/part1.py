from collections import defaultdict
from copy import deepcopy

conections = defaultdict(set)
with open('input1.txt') as f:
    for row in f.readlines():
        k, v = row.strip().split("-")
        conections[k].add(v)
        conections[v].add(k)

counter = 0

def dive(dic, node, ban_set):
    if node == 'end':
        global counter
        counter += 1
    elif node not in ban_set:
        
        
        if node[0].islower():
            ban_set.add(node)

        cur = dic.get(node, False)
        if cur:
            for n in cur:
                dive(deepcopy(dic), n, deepcopy(ban_set))

dive(conections, 'start', set())

print(counter)