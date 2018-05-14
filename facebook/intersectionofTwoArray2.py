class Solution(object):
    def intersect(self, nums1, nums2):
        res = list()
        if len(nums1) == 0 or len(nums2) == 0:
            return res
        
        if len(nums1) > len(nums2):
            for n in nums2:
                if n in nums1:
                    nums1.remove(n)
                    res.append(n)
        else:
            for n in nums1:
                if n in nums2:
                    nums2.remove(n)
                    res.append(n)
            
        return res