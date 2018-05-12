class Solution(object):
    def lca(self, root, p, q):
        if not root:
            return None
        
        if root == q or root == p:
            return root
        
        left_lca = self.lca(root.left, p, q)
        right_lca = self.lca(root.right, p, q)

        if left_lca and right_lca:
            return root
        
        if left_lca is not None:
            return left_lca
        return right_lca