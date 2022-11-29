#read lines from input2.txt, split them on " ", and append this list to a list called lines
with open("input2.txt") as f:
    lines = [line.split(" ") for line in f]

aim = 0
x = 0
depth = 0
for line in lines:
    if line[0] == "forward":
        x += int(line[1])
        depth += aim*int(line[1])
    elif line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])
print(depth*x)