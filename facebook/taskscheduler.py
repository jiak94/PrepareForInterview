class Solution(object):
    def leastInterval(self, tasks, n):
        helper = [0] * 26
        for x in tasks:
            helper[ord(x) - 65] += 1
        
        helper = sorted(helper, reverse=True)
        res = helper[0] * (n+1)-n
        for i in range(1, len(helper)):
            if helper[i] == helper[0]:
                res += 1
            else:
                break
        return max(res, sum(helper))
