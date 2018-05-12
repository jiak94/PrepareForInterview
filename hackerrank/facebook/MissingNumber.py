class Solution(object):
    def missingNumber(self, nums):
        container = [-1] * (len(nums) + 1)

        for num in nums:
            container[num] = 0
        
        for i in range(len(container)):
            if container[i] != 0:
                return i
        return -1