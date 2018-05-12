class Solution(object):
    def isPalindrome(self, s):
        a = list()
        for char in s:
            if char.isalpha() or char.isnumeric():
                a.append(char.lower())
        
        return "".join(a) == "".join(a[::-1])
        