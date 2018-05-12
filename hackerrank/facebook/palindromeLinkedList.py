class Solution(object):
    def isPalindrome(self, head):
        fast = slow = head
        while fast.next and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        slow = self.reverse(slow)

        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True

    
    def reverse(self, head):
        if head == None:
            return head
        
        p = head.next
        head.next = None
        
        while (p != None):
            r = p.next
            p.next = head
            head = p
            p = r
        return head