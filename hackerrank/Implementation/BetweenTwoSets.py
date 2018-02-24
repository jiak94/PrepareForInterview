'''
You will be given two arrays of integers. You will be asked to determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

Output Format

Print the number of integers that are considered to be between a and b.

link: https://www.hackerrank.com/challenges/between-two-sets/problem
'''
import sys

def getTotalX(a, b):
    ct = 0
    for i in xrange(max(a),min(b)+1):
        for j in a:
            if i%j!=0:
                break
        else:
            for k in b:
                if k%i!=0:
                    break
            else:
                ct+=1
    return ct

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    total = getTotalX(a, b)
    print total