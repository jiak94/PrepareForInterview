'''
Weighted Uniform Strings
link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
'''
import sys

def calculateWeight(s):
    points = list()
    points.append(ord(s[0])-96)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            points.append(points[i-1] + ord(s[i]) - 96)
        else:
            points.append(ord(s[i])-96)
    return points

s = raw_input().strip()
points = set(calculateWeight(s))
n = int(raw_input().strip())
for a0 in xrange(n):
    x = int(raw_input().strip())
    if x in points:
        print "Yes"
    else:
        print "No"
