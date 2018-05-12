class Solution(object):
    def bestTimeToSellStock(self, nums):
        local = overall = 0

        for i in range(len(nums)-1):
            local = max(local + nums[i+1]- nums[i], 0)
            overall = max(local, overall)
        
        return overall