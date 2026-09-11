# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

K, M = map(int, input().split())

lists = []

for _ in range(K):
    data = list(map(int, input().split()))
    lists.append(data[1:])

maximum = 0

for values in product(*lists):
    total = sum(x * x for x in values)
    result = total % M

    if result > maximum:
        maximum = result

print(maximum)