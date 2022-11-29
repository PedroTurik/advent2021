from collections import Counter

with open('input2.txt') as f:
    data = f.readlines()
    outputs = [x.strip().split('|')[1].split(' ')[1:] for x in data]
    displays = [x.strip().split('|')[0].split(' ')[:-1] for x in data]

full_set = {'a','b','c','d','e','f','g'}

UR = {'a','b','c','d','e','f','g'},
UP = {'a','b','c','d','e','f','g'},
UL = {'a','b','c','d','e','f','g'},
MI = {'a','b','c','d','e','f','g'},
DR = {'a','b','c','d','e','f','g'},
DL = {'a','b','c','d','e','f','g'},
DO = {'a','b','c','d','e','f','g'}

segments = [UR,UP,UL,MI,DR,DL,DO]

number_structure = {
    0: [UP, UR, UL, DR, DL, DO],
    1: [UR, DR],
    2: [UP, UR, MI, DL, DO],
    3: [UP, UR, MI, DR, DO],
    4: [UL, UR, MI, DR],
    5: [UP, UL, MI, DR, DO],
    6: [UP, UL, MI, DR, DL, DO],
    7: [UP, UR, DR],
    8: [UP, UR, UL, MI, DR, DL, DO],
    9: [UP, UR, UL, MI, DR, DO]
}


def mark_known(segments, known):
    for segment in segments:
        if len(segment) > 1: segment -= known

def infer_output(display, output):
    for num in display:
        if len(num) == 


