class Solution(object):
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0:
            return 0
        rooms = 0
        res = 0

        start = list()
        end = list()
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        
        start = sorted(start)
        end = sorted(end)

        i = j = 0
        while i < len(start):
            rooms += 1
            while end[j] <= start[i]:
                rooms -= 1
                j += 1
            i += 1
            res = max(res, rooms)

        return res
