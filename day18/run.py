from snail_functions import *


def main():
    with open("input.txt") as f:
        snails = [eval(row.strip()) for row in f]

    acc = snails[LEFT]
    for s in snails[1:]:
        acc = add_snail(acc, s)
        reduce(acc)

    print(calculate_magnitude(acc))


if __name__ == "__main__":
    main()