'''
Steve has a string, , consisting of  lowercase English alphabetic letters. In one operation, he can delete any pair of adjacent letters with same value. For example, string "aabcc" would become either "aab" or "bcc" after  operation.

Steve wants to reduce  as much as possible. To do this, he will repeat the above operation as many times as it can be performed. Help Steve out by finding and printing 's non-reducible form!

link: https://www.hackerrank.com/challenges/reduced-string/problem
'''
import sys

def consecutive_index(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return i
    
    return -1

def super_reduced_string(s):
    while consecutive_index(s) != -1:
        idx = consecutive_index(s)
        s = s[:idx] + s[idx+2:]
    
    if len(s) == 0:
        return "Empty String"
    return s

s = raw_input().strip()
result = super_reduced_string(s)
print(result)