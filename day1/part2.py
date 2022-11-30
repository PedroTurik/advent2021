#read lines from input2.txt, transform them into integers, and append them to a list
with open("input1.txt") as f:
    lines = [int(line) for line in f]

#count the number of times the sum of a sliding window of 3 numbers increases in comparison to the previous window
def count_increasing_windows(numbers):
    count = 0
    for i in range(len(numbers) - 2):
        if numbers[i] + numbers[i + 1] + numbers[i + 2] > numbers[i - 1] + numbers[i] + numbers[i + 1]:
            count += 1
    return count

print(count_increasing_windows(lines))