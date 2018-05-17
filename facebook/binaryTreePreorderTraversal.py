class Solution(object):
    def preorderTraversal(self, root):
        res = list()
        if not root:
            return res
        
        res += [root.val]
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res