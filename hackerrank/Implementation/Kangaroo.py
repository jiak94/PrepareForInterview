'''
There are two kangaroos on a number line ready to jump in the positive 
direction. Each kangaroo takes the same amount of time to make a jump, 
regardless of distance. That is, if kangaroo one jumps 3 meters and 
kangaroo two jumps 5 meters, they each do it in one second, for example.

Given the starting locations and jump distances for each kangaroo, 
determine if and when they will land at the same location at the 
same time.

Output Format

Print YES if they can land on the same location at the same time; otherwise, print NO.

link: https://www.hackerrank.com/challenges/kangaroo/problem
'''
import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if v1 <= v2:
        return "NO"
        
    while (x1 < x2):
        x1 += v1
        x2 += v2
    if x1 == x2:
        return "YES"
    else:
        return "NO"

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)