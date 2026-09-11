# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

lower = sorted([c for c in s if c.islower()])
upper = sorted([c for c in s if c.isupper()])
odd = sorted([c for c in s if c.isdigit() and int(c) % 2 != 0])
even = sorted([c for c in s if c.isdigit() and int(c) % 2 == 0])

print(''.join(lower + upper + odd + even))