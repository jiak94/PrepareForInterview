class Solution(object):
    def binaryTreePaths(self, root):
        res = list()

        if root is None:
            return res
        
        self.get_path(self, root, str(root.val), res)
        return res
    
    def get_path(self, root, current, res):
        if root is None:
            return
        
        
        if root.left is None and root.right is None:
            res.append(current)
        
        if root.left is not None:
            self.get_path(root.left, current + "->" + str(root.left.val), res)
        if root.right is not None:
            self.get_path(root.right, current+ "->" + str(root.right.val), res)