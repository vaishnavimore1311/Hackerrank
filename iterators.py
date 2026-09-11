# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

count = 0
total = 0

for combination in combinations(range(n), k):
    total += 1

    for index in combination:
        if letters[index] == 'a':
            count += 1
            break

print(count / total)