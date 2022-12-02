from collections import defaultdict
from functools import cache
with open('input1.txt') as f:
    start = f.readline()
    f.readline()
    template = {}
    for row in f.readlines():
        a, b = row.strip().split(' -> ')
        template[a] = b

apperances= defaultdict(int)
for c in start.strip():

    apperances[c] += 1


@cache
def add_letter(pair, depth):
    tmp = defaultdict(int)

    if depth == 0:
        return tmp

    result = template[pair]
    tmp[result] += 1

    for k, v in add_letter(pair[0] + result, depth-1).items():
        tmp[k] += v

    for k, v in add_letter(result + pair[1], depth-1).items():
        tmp[k] += v
    
    return tmp
steps = int(input("enter number of steps "))
for i in range(2, len(start)):
    for k, v in add_letter(start[i-2:i], steps).items():
        apperances[k] += v

print(max(apperances.values()) - min(apperances.values()))
