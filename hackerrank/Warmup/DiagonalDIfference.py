'''
Given a square matrix, 
calculate the absolute difference between the sums of its diagonals.

Output Format

Print the absolute difference between
the sums of the matrix's two diagonals as a single integer.

link: https://www.hackerrank.com/challenges/diagonal-difference/problem
'''

import sys

def diagonalDifference(a):
    dia_1 = 0
    dia_2 = 0
    for i in range(len(a)):
        dia_1 += a[i][i]
    
    for i in range(len(a)):
        dia_2 += a[i][len(a)-1-i]
    
    return abs(dia_2 - dia_1)
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
        a_temp = map(int,raw_input().strip().split(' '))
        a.append(a_temp)
    result = diagonalDifference(a)
    print result