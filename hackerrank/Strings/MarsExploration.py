'''
Mars Exploration
link: https://www.hackerrank.com/challenges/mars-exploration/problem
'''

import sys
MESSAGE = "SOS"
def marsExploration(s):
    res = 0
    i = 0
    while i < len(s) - 2:
        string = s[i:i+3];
        # print string
        if string is not MESSAGE:
            for j in range(3):
                if string[j] != MESSAGE[j]:
                    res += 1
        i += 3
    return res

if __name__ == "__main__":
    s = raw_input().strip()
    result = marsExploration(s)
    print result