class Solution(object):
    def hammingDistance(self, x, y):
        z = x ^ y
        res = 0
        while z != 0:
            res += z % 2
            z = z >> 1
        return res