'''
String  always consists of two distinct alternating characters. For example, if string 's two distinct characters are x and y, then t could be xyxyx or yxyxy but not xxyy or xyyx.

You can convert some string  to string  by deleting characters from . When you delete a character from , you must delete all occurrences of it in . For example, if  abaacdabd and you delete the character a, then the string becomes bcdbd.

Given , convert it to the longest possible string . Then print the length of string  on a new line; if no string  can be formed from , print  instead.

link: https://www.hackerrank.com/challenges/two-characters/problem
'''
import sys, itertools

def characters(s):
    res = list()
    for i in s:
        if i not in res:
            res.append(i)
    return res

def valid(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

def remove(s, chars):
    new_str = ""
    for i in range(len(s)):
        if s[i] not in chars:
            new_str += s[i]
    return new_str

def twoCharaters(s):
    chars = characters(s)
    if len(chars) < 2:
        return 0
    if len(chars) == 2:
        if valid(s):
            return len(s)
        return 0

    combinations = itertools.combinations("".join(chars), len(chars) - 2)
    max_len = 0
    for com in combinations:
        tmp = remove(s, com)
        if valid(tmp) and len(tmp) > max_len:
            max_len = len(tmp)
    
    return max_len
        

if __name__ == "__main__":
    l = int(raw_input().strip())
    s = raw_input().strip()
    result = twoCharaters(s)
    print result