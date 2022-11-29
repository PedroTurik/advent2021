# read lines from input1.txt and split them on " ", then add the second element to a variable called f if the first element is "foward", add to a variable called d if the first element is "down", and add to a variable called u if the first element is "up", then print f*(d-u)
with open("input1.txt") as f:
    lines = [line.split(" ") for line in f]
    f = 0
    d = 0
    u = 0
    for line in lines:
        if line[0] == "forward":
            f += int(line[1])
        elif line[0] == "down":
            d += int(line[1])
        elif line[0] == "up":
            u += int(line[1])
    print(f*(d-u))

