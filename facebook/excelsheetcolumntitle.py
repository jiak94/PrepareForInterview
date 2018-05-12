class Solution(object):
    def convertToTitle(self, n):
        c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = list()
        while n != 0:
            r = n % 26
            n = n /26
            if r == 0:
                res.insert(0, c[25])
                n -= 1
            else:
                res.insert(0, c[r-1])
        
        return "".join(res) 


