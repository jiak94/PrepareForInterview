class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return False
        
        pivot = len(nums)

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                pivot = i
        
        left = nums[:pivot]
        right = nums[pivot:]

        return self.bSearch(left, target) or self.bSearch(right, target)
    
    def bSearch(self, nums, target):
        if len(nums) == 0:
            return False
        if target > nums[-1] or target < nums[0]:
            return False
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)/2
            if nums[mid] == target:
                return True
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
