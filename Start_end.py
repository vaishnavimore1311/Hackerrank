# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
k = input()
matches = re.finditer(f'(?={k})', s)
found = False
for match in matches:
    found = True
    print((match.start(), match.start() + len(k) - 1))
if not found:
    print((-1, -1))