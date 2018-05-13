class Solution(object):
    def multiply(self, num1, num2):
        if not num1 or not num2:
            return 0
        
        res = [0] * (len(num1) + len(num2))
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                p = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                
                if res[p2] + p % 10 >= 10:
                    res[p2] += p % 10
                    res[p2] -= 10
                    res[p2-1] += 1
                else:
                    res[p2] += p % 10
                
                if res[p1] + p/10 >= 10:
                    res[p1] += p/10
                    res[p1] -= 10
                    res[p1-1] += 1
                else:
                    res[p1] += p / 10
        s = ""
        omit = True
        for num in res:
            if num != 0:
                omit = False
            if omit and num == 0:
                continue
            s += str(num)
        if len(s) == 0:
            return "0"
        return s