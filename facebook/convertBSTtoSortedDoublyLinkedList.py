class Solution(object):
    def treeToDoublyList(self, root):
        if not root:
            return root
        
        inorder = self.inorder(root)

        if len(inorder):
            node = Node(inorder[0], None, None)
            node.left = node
            node.right = node
            return node
        
        head = Node(inorder[0], None, None)
        tail = Node(inorder[-1], head, head)
        head.left = tail
        head.right = head
        prev = head

        for i in len(inorder-1):
            if i == len(inorder) - 2:
                node = Node(inorder[i], prev, tail)
                tail.left = node
                prev.right = node
            else:
                node = Node(inorder[i], prev, None)
                prev.right = node
                prev = prev.right
        return head

    def inorder(self, root):
        res = list()
        if not root:
            return res
        
        res += self.inorder(root.left)
        res += [root.val]
        res += self.inorder(root.right)