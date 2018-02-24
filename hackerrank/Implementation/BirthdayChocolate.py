'''
Lily has a chocolate bar consisting of a row of  squares where 
each square has an integer written on it. She wants to share 
it with Ron for his birthday, which falls on month m and day d.
Lily wants to give Ron a piece of chocolate only if it contains
m consecutive squares whose integers sum to d.

Output Format

Print an integer denoting the total number of ways that Lily can give a piece of chocolate to Ron.

link: https://www.hackerrank.com/challenges/the-birthday-bar/problem
'''
import sys

def solve(n, s, d, m):
    if n < m:
        if sum(s) == d:
            return 1
        else:
            return 0 
    chunks = list()
    for i in range(n):
        if i + m <= n:
            sublist = s[i:i+m]
            chunks.append(sublist)
        else:
            break
    count = 0
    for chunk in chunks:
        if sum(chunk) == d:
            count += 1
    return count

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)