class Solution(object):
    def reorderList(self, head):
        if not head:
            return head
        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        res = ListNode(-1)
        
        slow = self.reverse(slow)
        while slow and slow.next:
            target = slow
            slow = slow.next
            target.next = head.next
            head.next = target
            head = head.next.next
        
    
    def reverse(self, head):
        if not head:
            return head
        
        p = head.next
        head.next = None
        
        while p:
            r = p.next
            p.next = head
            head = p
            p = r
        return head