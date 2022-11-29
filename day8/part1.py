with open('input1.txt') as f:
    data = f.readlines()
    output = [x.strip().split('|')[1].split(' ')[1:] for x in data]

counter = 0

for out in output:
    for n in out:
        if len(n) in [2, 4, 3, 7]:
            counter += 1

print(counter)