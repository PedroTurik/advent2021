with open('input1.txt', 'r') as f:
    positions = [int(x) for x in f.readline().strip().split(',')]

s = set(positions)

less_fuel = 100000000
for pos in s:
    cur_fuel = 0
    for crab in positions:
        cur_fuel += sum(range(abs(crab-pos)+1))
    if cur_fuel < less_fuel:
        less_fuel = cur_fuel

print(less_fuel)

