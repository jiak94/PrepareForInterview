'''
Big Sorting
link: https://www.hackerrank.com/challenges/big-sorting/problem
'''
import sys

def bigSorting(arr):
    res = list()
    d = dict()
    for i in arr:
        if len(str(i)) in d:
            d[len(str(i))].append(i)
        else:
            d[len(str(i))] = [i]
    for key in sorted(d.iterkeys()):
        res += sorted(d[key])
        
    return res

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = []
    arr_i = 0
    for arr_i in xrange(n):
        arr_t = str(raw_input().strip())
        arr.append(arr_t)
    result = bigSorting(arr)
    print "\n".join(map(str, result))