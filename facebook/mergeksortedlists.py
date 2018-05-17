class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        nodes = list()
        
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        if len(nodes) == 0:
            return None
        nodes = sorted(nodes)

        head = ListNode(nodes[0])
        dummy_head = head

        for i in range(1, len(nodes)):
            dummy_head.next = ListNode(nodes[i])
            dummy_head = dummy_head.next
        
        return head
