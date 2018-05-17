class Solution(object):
    def missingNumber(self, nums):
        container = [-1] * (len(nums) + 1)

        for num in nums:
            container[num] = 0
        
        for i in range(len(container)):
            if container[i] != 0:
                return i
        return -1
    # solution 2
    def missingNumber2(self, nums):
        n = len(nums)
        helper = [-1] * (n+1)
        for i in range(n):
            helper[nums[i]] = 1
        return helper.index(-1)