with open('input.txt') as f:
    a = f.read().split("\n\n")

def check_overlap(points, scanner):
    for point in points:
        x, y, z = point





scanners = []
for x in a:
    curScan = []
    for line in x.split('\n')[1:]:
        curScan.append(tuple(map(int, line.split(','))))
    scanners.append(tuple(curScan))

scanners = scanners

points = set(scanners.pop(0))

while scanners:
    for i, scanner in enumerate(scanners):
        a = check_overlap(points, set(scanner))
        if a:
            scanners.pop(i)
            points.update(a)
            break

