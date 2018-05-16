class Solution(object):
    def flatten(self, root):
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)

        tmp_root = root
        if not tmp_root.left:
            return
        
        tmp_root = tmp_root.left
        while tmp_root.right:
            tmp_root = tmp_root.right
        
        tmp_root.right = root.right
        root.right = root.left
        root.left = None
        return