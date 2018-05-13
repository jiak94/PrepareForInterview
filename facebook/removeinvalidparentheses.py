class Solution(object):
    def removeInvalidParentheses(self, s):
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            if s[i] == ")":
                if l > 0:
                    l -= 1
                else:
                    r += 1
        res = list()
        self.dfs(res, s, l, r, 0)
        return res
    def dfs(self, res, s, l, r, start):
        if r == 0 and l == 0 and self.valid(s):
            res.append(s)
        
        for i in range(start, len(s)):
            if i != start and s[i] == s[i - 1]:
                continue
            if s[i] == "(":
                n = s[:i] + s[i+1:]
                if l > 0:
                    self.dfs(res, n, l - 1, r, i)
            if s[i] == ")":
                n = s[:i] + s[i+1:]
                if r > 0:
                    self.dfs(res, n, l, r - 1, i)
    
    def valid(self, s):
        c = 0
        for i in range(len(s)):
            if s[i] == "(":
                c += 1
            if s[i] == ")":
                c -= 1
                if c < 0:
                    return False
        return c == 0
        