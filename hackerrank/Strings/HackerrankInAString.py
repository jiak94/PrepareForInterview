'''
HackerRank in a String
link: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
'''
import sys
HACKERRANK = "hackerrank"
def hackerrankInString(s):
    for i in HACKERRANK:
        idx = s.find(i)
        if idx < 0:
            return "NO"
        s = s[idx+1:]
    return "YES"

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        result = hackerrankInString(s)
        print result