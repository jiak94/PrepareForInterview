class Solution(object):
    def subarraySum(self, nums, k):
        ht = {0:1}
        res = s = 0
        for num in nums:
            s += num
            if s-k in ht:
                res += ht[s-k]
            if s in ht:
                ht[s] += 1
            else:
                ht[s] = 1
        return res