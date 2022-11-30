from collections import defaultdict
from copy import deepcopy

conections = defaultdict(set)
with open('input1.txt') as f:
    for row in f.readlines():
        k, v = row.strip().split("-")
        conections[k].add(v)
        conections[v].add(k)

counter = 0

def dive(dic, node, ban_set, repeats):
    if repeats > 1:
        return
    if node == 'end' and repeats == 1:
        global counter
        counter += 1
    if node in ban_set:
        repeats += 1
    else:
        if node[0].islower():
            ban_set.add(node)
    cur = dic.get(node, False)
    if cur:
        for n in cur:
            dive(deepcopy(dic), n, deepcopy(ban_set), repeats)

dive(conections, 'start', set(), 0)

print(counter + 4338)








4338