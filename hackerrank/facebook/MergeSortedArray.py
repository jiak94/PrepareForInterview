class Solution(object):
    def merge(self, num1, m, num2, n):
        i = j = 0
        while i < m and j < n:
            if num1[i] < num2[j]:
                i += 1
            else:
                num1.insert(i, num2[j])
                num1.pop()
                i += 1
                j += 1
                m += 1
        while j < n:
            num1.insert(i, num2[j])
            num1.pop()
            i += 1
            j += 1