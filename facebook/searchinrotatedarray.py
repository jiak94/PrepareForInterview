    def search(self, nums, target):
        if not nums:
            return -1
        
        split_point = -1
        for i in range(len(nums)):
            if i != 0 and nums[i] < nums[i-1]:
                split_point = i
                break
        if split_point == -1:
            return self.bSearch(nums, target)
        l = nums[:split_point]
        r = nums[split_point:]
        
        if target >= nums[0]:
            return self.bSearch(l, target)
        else:
            res = self.bSearch(r, target)
            if res != -1:
                return res + split_point
            return res
    
    def bSearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = int((start + end)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid + 1
        return -1