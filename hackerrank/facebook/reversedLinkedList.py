class Solution(object):
    def reversedLinkedList(self, head):
        if not head:
            return head
        
        p = head.next
        head.next = None

        while p is not None:
            r = p.next
            p.next = head
            head = p
            p = r
        
        return head