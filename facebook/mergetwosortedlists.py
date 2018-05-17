class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy_head = ListNode(-1)
        head = dummy_head

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                dummy_head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                dummy_head.next = ListNode(l2.val)
                l2 = l2.next
            
            dummy_head = dummy_head.next
        
        if l1:
            dummy_head.next = l1
        
        if l2:
            dummy_head.next = l2
        
        return head.next