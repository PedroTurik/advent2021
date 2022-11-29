with open("input1.txt") as f:
    binarios = [line.strip() for line in f]

oxi = [x for x in binarios]
co2 = [x for x in binarios]

cur_col = 0
while len(oxi) != 1:
    um = 0
    zero = 0
    for row in oxi:
        if row[cur_col] == "1":
            um += 1
        else:
            zero += 1
    oxi = [x for x in oxi if x[cur_col] == ('1' if um >= zero else '0')]
    cur_col += 1

cur_col = 0
while len(co2) != 1:
    um = 0
    zero = 0
    for row in co2:
        if row[cur_col] == "1":
            um += 1
        else:
            zero += 1
    co2 = [x for x in co2 if x[cur_col] == ('1' if um < zero else '0')]
    cur_col += 1


print(int(oxi[0], 2) * int(co2[0], 2))



