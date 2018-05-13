class Solution(object):
    def myPow(self, x, n):
        N = n
        if N < 0:
            x = 1/x
            N = -N
        
        return self.fastpow(x, N)
    def fastpow(self, x, n):
        if n == 0:
            return 1.0
        
        half = self.fastpow(x, n/2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x