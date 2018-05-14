class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        
        root = preorder[0]
        pivot = -1
        for i in range(len(inorder)):
            if inorder[i] == root:
                pivot = i
                break
        if pivot == -1:
            return None
        
        
        left_inorder = inorder[:pivot]
        right_inorder = inorder[pivot+1:]
        
        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1:]
        
        ret = TreeNode(root)
        ret.left = self.buildTree(left_preorder, left_inorder)
        ret.right = self.buildTree(right_preorder, right_inorder)
        return ret