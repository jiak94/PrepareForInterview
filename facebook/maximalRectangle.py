class Solution(object):
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        height = [0] * n
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    height[j] = 0
                    continue
                height[j] += 1
                Min = height[j]

                for k in range(j+1)[::-1]:
                    Min = min(height[k], Min)
                    res = max(res, (j-k+1) * Min)
        return res