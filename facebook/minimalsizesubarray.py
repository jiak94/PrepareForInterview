class Solution(object):
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        if n == 0:
            return n
        res = n + 1

        left = right = total = 0
        while right < n:
            while right < n and total < s:
                total += nums[right]
                right += 1
            if total < s:
                break
            
            while left < right and total >= s:
                total -= nums[left]
                left += 1
            res = min(res, right - left + 1)
        if res == n+1:
            return 0
        return res