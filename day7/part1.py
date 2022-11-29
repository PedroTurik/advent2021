from statistics import median


with open('input1.txt', 'r') as f:
    positions = [int(x) for x in f.readline().strip().split(',')]

med = int(median(positions))

fuel_used = 0
for pos in positions:
    fuel_used += abs(pos - med)

print(fuel_used)