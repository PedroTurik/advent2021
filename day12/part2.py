from collections import defaultdict
from copy import deepcopy

conections = defaultdict(set)
with open('input1.txt') as f:
    for row in f.readlines():
        k, v = row.strip().split("-")
        conections[k].add(v)
        conections[v].add(k)

counter = 0

def dive(dic, node, ban_set, repeats, first=False):
    if node == 'start' and not first:
        return
    if node == 'end':
        if repeats == 1:
            global counter
            counter += 1
        return

    new_repeats = repeats

    if node in ban_set:
        new_repeats = repeats + 1
    else:
        if node[0].islower():
            ban_set.add(node)


    if repeats > 1:
        return


    cur = dic.get(node, False)
    if cur:
        for n in cur:
            dive(dic, n, deepcopy(ban_set), new_repeats, False)

dive(conections, 'start', set(), 0, first=True)

print(counter + 4338)











4338