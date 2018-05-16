class Solution(object):
    def getIntersectionNode(self, headA, headB):
        n1 = headA
        n2 = headB
        l1 = l2 = 0

        while n1:
            l1 += 1
            n1 = n1.next
        
        while n2:
            l2 += 1
            n2 = n2.next
        
        while l1 > l2:
            headA = headA.next
            l1 -= 1
        
        while l2 > l1:
            headB = headB.next
            l2 -= 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA