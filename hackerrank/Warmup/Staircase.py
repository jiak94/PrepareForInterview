'''
Consider a staircase of size : 4

   #
  ##
 ###
####

Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces.
The last line is not preceded by any spaces.

Output Format

Print a staircase of size n using # symbols and spaces.

link: https://www.hackerrank.com/challenges/staircase/problem
'''

import sys

def staircase(n):
    for i in range(1, n + 1):
        print " " * (n-i) + "#"*i

if __name__ == "__main__":
    n = int(raw_input().strip())
    staircase(n)