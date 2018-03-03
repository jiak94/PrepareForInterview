'''
Pangrams
link: https://www.hackerrank.com/challenges/pangrams/problem
'''
import sys

def pangrams(s):
    s = s.replace(" ", "")
    if len(s) < 26:
        return "not pangram"
    letters = list()
    for i in s:
        if i.lower() not in letters and i.isalpha():
            letters.append(i.lower())
    # print sorted(letters)
    if len(letters) != 26:
        return "not pangram"
    return "pangram"

if __name__ == "__main__":
    s = raw_input().strip()
    result = pangrams(s)
    print result