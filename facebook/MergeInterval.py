class Solution(object):
    def merge(self, intervals):
        res = list()
        for i in sorted(intervals, key=lambda i:i.start):
            if len(res) != 0 and i.start <= res[-1].end:
                if i.end >= res[-1].end:
                    res[-1].end = i.end
            else:
                res.append(i)
        return res