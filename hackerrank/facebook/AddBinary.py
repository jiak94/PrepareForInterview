class Solution(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = list()

        while i >= 0 and j >= 0:
            tmp = int(a[i]) + int(b[j]) + carry
            carry = 0
            if tmp > 1:
                carry = 1
            res.append(str(tmp % 2))
            i -= 1
            j -= 1
        
        while i >= 0:
            tmp = int(a[i]) + carry
            carry = 0
            if tmp > 1:
                carry = 1
            res.append(str(tmp % 2))
            i -= 1
        
        while j >= 0:
            tmp = int(b[j]) + carry
            carry = 0
            if tmp > 1:
                carry = 1
            res.append(str(tmp % 2))
            j -= 1
        
        if carry != 0:
            res.append(str(carry))
        
        return ''.join(res[::-1])