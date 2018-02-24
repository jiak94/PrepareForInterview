'''
You are given an array of integers, and a positive integer, k.
Find and print the number of i, j pairs where i < j and a_i + a_j
is divisible by k

link: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
'''
import sys

def divisibleSumPairs(n, k, ar):
    combinations = list()
    for i in range(n):
        for j in range(i+1, n):
            combinations.append([ar[i], ar[j]])
    
    count = 0
    for pair in combinations:
        if sum(pair) % k == 0:
            count += 1
    return count

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)