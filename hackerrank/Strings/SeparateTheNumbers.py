'''
separate the numbers
link: https://www.hackerrank.com/challenges/separate-the-numbers/problem
'''
import sys

def separateNumbers(s):
    if s[0] == '0':
        print "NO"
        return
    if len(s) < 1:
        print "NO"
        return
    # Complete this function
    for i in range(1, len(s)):
        new_str = s[0:0+i]
        rest = s[i:]
       
        if len(rest) < len(new_str):
            print "NO"
            return
        int_str = int(new_str)
        
        while s != "":
            int_str += 1
            # print "int_str" + str(int_str)
            if rest.find(str(int_str)) != 0:
                break;
            else:
                rest = rest[len(str(int_str)):]
                # print "rest: " + rest
            
        if rest == "":
            print "YES " + new_str
            return
    print "NO"

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        separateNumbers(s)