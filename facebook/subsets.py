import copy
class Solution(object):
    def subsets(self, nums):
        nums = sorted(nums)
        res = list()
        self.dfs(res, [], nums, 0)

        return res
        
    def dfs(self, res, l, nums, pos):
        res.append(copy.deepcopy(l))

        for i in range(pos, len(nums)):
            l.append(nums[i])
            self.dfs(res, l, nums, pos + 1)
            l.pop()