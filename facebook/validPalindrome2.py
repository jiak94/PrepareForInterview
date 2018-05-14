class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s - 1)

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                break
        if left >= right
            return True
        return self.isPalindrome(s[:left] + s[left+1:]) or self.isPalindrome(s[:right]+s[right+1:])
    
    def isPalindrome(self, s):
        return s == s[::-1]