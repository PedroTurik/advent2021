from copy import deepcopy
import helper

with open('input1.txt') as f:
    snail_numbers = [eval(a) for a in f.readlines()]


cur_snail = snail_numbers.pop(0)

while snail_numbers:
    result = [cur_snail, snail_numbers.pop(0)]
    while True:
        aux, check = helper.clean(deepcopy(result))
        if not check:
            break
        else:
            result = aux[0]
        helper.SPLIT_CHANGED = False
    cur_snail = aux

print(helper.magnitude(cur_snail))