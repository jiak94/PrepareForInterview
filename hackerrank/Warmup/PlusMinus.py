'''
Given an array of integers, calculate which fraction of its elements 
are positive, which fraction of its elements are negative, 
and which fraction of its elements are zeroes, respectively. 
Print the decimal value of each fraction on a new line.

Output Format

You must print the following 3 lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeroes in the array compared to its size.

link: https://www.hackerrank.com/challenges/plus-minus/problem
'''
import sys

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    
    print("%.6f" % (pos/float(len(arr))))
    print("%.6f" % (neg/float(len(arr))))
    print("%.6f" % (zero/float(len(arr))))

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    plusMinus(arr)