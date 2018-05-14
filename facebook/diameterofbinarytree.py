class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.best = 1
        self.depth(root)
        return self.best - 1
    def depth(self, root):
        if not root:
            return 0
        
        left = self.depth(root.left)
        right = self.depth(root.right)
        self.best = max(self.best, left + right + 1)
        return 1 + max(left, right)