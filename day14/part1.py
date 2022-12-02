from collections import defaultdict
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


def add_letter(pair, depth):
    if depth == 0:
        return

    result = template[pair]
    apperances[result] += 1

    add_letter(pair[0] + result, depth-1)
    add_letter(result + pair[1], depth-1)

for i in range(2, len(start)):
    print("oi")
    add_letter(start[i-2:i], 20)

print(max(apperances.values()) - min(apperances.values()))



