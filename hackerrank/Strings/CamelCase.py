'''
Alice wrote a sequence of words in CamelCase as a string of letters, , having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given , print the number of words in  on a new line.

link: https://www.hackerrank.com/challenges/camelcase/problem
'''
import sys

def camelcase(s):
    if len(s) == 0:
        return 0
    ct = 0
    for character in s:
        if ord(character) >= ord('A') and ord(character) <= ord('Z'):
            ct += 1
    return ct+1

if __name__ == "__main__":
    s = raw_input().strip()
    result = camelcase(s)
    print result