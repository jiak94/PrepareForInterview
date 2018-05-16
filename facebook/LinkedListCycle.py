class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False