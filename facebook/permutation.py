class Solution(object):
    def permute(self, nums):
        res = list()
        ss = list()
        self.dfs(nums, ss, res)
        return res
    def dfs(self, nums, ss, res):
        if len(nums) == len(nums):
            res.append(ss)
            return
        for i in set(nums) - set(ss):
            self.dfs(nums, ss + [i], res)