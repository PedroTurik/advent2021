from copy import deepcopy
from snail_functions import *


def main():
    with open("input.txt") as f:
        snails = [eval(row.strip()) for row in f]

    maxo = 0

    for i, s1 in enumerate(snails):
        for j, s2 in enumerate(snails):
            if i != j:
                s = add_snail(deepcopy(s1), deepcopy(s2))
                reduce(s)
                maxo = max(calculate_magnitude(s), maxo)

    print(maxo)



if __name__ == "__main__":
    main()