class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        res = list()
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    tmp = list()
                    tmp.append(nums[i])
                    tmp.append(nums[left])
                    tmp.append(nums[right])
                    res.append(tmp)
                    while left < len(nums)-1 and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while right >= 1 and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    right -= 1
        
        return res