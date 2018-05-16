class Solution(object):
    def maxSubArrayLen(self, nums, k):
        prefix_sum = 0
        dic = {0:-1}
        res = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in dic:
                res = max(res, i - dic[prefix_sum - k])
            if prefix_sum not in dic:
                dic[prefix_sum] = i
        
        return res