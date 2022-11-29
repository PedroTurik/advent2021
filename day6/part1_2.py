import collections


with open('input1.txt', 'r') as f:
    fishes = [int(x) for x in f.readline().split(',')]

n_of_fish = {x:0 for x in range(9)}


for n in fishes:
    n_of_fish[n] += 1



for _ in range(256):
    prev = 0
    for age in range(8, -1, -1):
        n = n_of_fish[age]
        n_of_fish[age] = prev
        prev = n
    n_of_fish[8] = prev
    n_of_fish[6] += prev
   

print(sum(n_of_fish.values()))

