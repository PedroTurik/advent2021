from collections import Counter

with open('input2.txt') as f:
    data = f.readlines()
    outputs = [x.strip().split('|')[1].split(' ')[1:] for x in data]
    displays = [x.strip().split('|')[0].split(' ')[:-1] for x in data]


formulas = {
    1: set(),
    4: set(),
    7: set(),
    8: set()
}