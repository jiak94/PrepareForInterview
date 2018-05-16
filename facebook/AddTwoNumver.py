class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(-1)
        head = dummy_head

        carry = 0

        while l1 and l2:
            res = l1.val + l2.val + carry
            carry = 0
            if res >= 10:
                carry = res / 10
                res = res % 10
            
            new_node = ListNode(res)
            l1 = l1.next
            l2 = l2.next
            dummy_head.next = new_node
            dummy_head = dummy_head.next
        
        while l1:
            res = l1.val + carry
            carry = 0
            if res >= 10:
                carry = res /10
                res = res % 10
            new_node = ListNode(res)
            l1 = l1.next

            dummy_head.next = new_node
            dummy_head = dummy_head.next
        
        while l2:
            res = l2.val + carry
            carry = 0
            if res >= 10:
                carry = res / 10
                res = res % 10
            
            new_node = ListNode(res)
            l2 = l2.next
            
            dummy_head.next = new_node
            dummy_head = dummy_head.next
        
        if carry > 0:
            new_node = ListNode(carry)
            dummy_head.next = new_node
            dummy_head = dummy_head.next
        
        return head.next