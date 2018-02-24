'''
Given five positive integers, find the minimum and maximum values 
that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single
line of two space-separated long integers.

Output Format

Print two space-separated long integers denoting the respective minimum
and maximum values that can be calculated by summing exactly
four of the five integers. (The output can be greater than a 32 
bit integer.)

link: https://www.hackerrank.com/challenges/mini-max-sum/problem
'''
import sys

def miniMaxSum(arr):
    all_sum = sum(arr)
    print("%d %d" % (all_sum-min(arr) , all_sum-max(arr)))
if __name__ == "__main__":
    arr = map(int, raw_input().strip().split(' '))
    miniMaxSum(arr)