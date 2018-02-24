'''
Given an array of integers, find the sum of its elements.

Output Format:
Print the sum of the array's elements as a single integer.

link: https://www.hackerrank.com/challenges/simple-array-sum/problem

'''

import sys

def simpleArraySum(n, ar):
    res = 0
    for n in ar:
        res += n
    return res
    
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
