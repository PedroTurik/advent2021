# read lines from "input.txt", tranform them into integers, and append them to a list
with open("input1.txt") as f:
    lines = [int(line) for line in f]


# count the number of times a number in the list is greater than the number before it
def count_increasing_numbers(numbers):
    count = 0
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i - 1]:
            count += 1
    return count

print(count_increasing_numbers(lines))