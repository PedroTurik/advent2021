with open("input.txt") as f:
    snails = [eval(row.strip()) for row in f]


def calculate_magnitude(snail):
    if type(snail) == int:
        return snail

    return 3*calculate_magnitude(snail[0]) + 2*calculate_magnitude(snail[1])




