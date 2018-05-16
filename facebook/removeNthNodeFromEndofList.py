class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy_head = ListNode(-1)
        dummy_head.next = head

        slow, fast = dummy_head
        i = 0
        while i < n and fast:
            fast = fast.next
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy_head.next