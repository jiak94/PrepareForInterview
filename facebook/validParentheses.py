class Solution(object):
    def isValid(self, s):
        q = list()
        
        for char in s:
            if char == ")":
                if len(q) == 0:
                    return False
                elif q[-1] != "(":
                    return False
                else:
                    q.pop()
            elif char == "]":
                if len(q) == 0:
                    return False
                elif q[-1] != "[":
                    return False
                else:
                    q.pop()
            elif char == "}":
                if len(q) == 0:
                    return False
                elif q[-1] != "{":
                    return False
                else:
                    q.pop()
            else:
                q.append(char)
        
        return len(q) == 0