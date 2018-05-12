class Solution(object):
    def moveZeros(self, nums):
        left = right = 0

        while right < len(nums):
            while nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
    