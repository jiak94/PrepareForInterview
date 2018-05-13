class Solution(object):
    def productExceptSelf(self, nums):
        a = len(nums) * [1]
        b = len(nums) * [1]
        
        for i in range(1, len(nums)):
            a[i] = nums[i-1] * a[i-1]
        
        for i in reversed(range(len(nums)-1)):
            b[i] = nums[i+1] * b[i+1]
        
        return [i*j for i,j in zip(a,b)]