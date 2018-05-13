class BSTIterator(object):
    def __init__(self, root):
        self.stack = list()
        if not root:
            return
        while root:
            self.stack.append(root)
            root = root.left
    
    def hasNext(self):
        if len(self.stack) == 0:
            return False
        return True
    
    def next(self):
        node = self.stack.pop()
        res = node.val
        node = node.right
        
        
        while node:
            self.stack.append(node)
            node = node.left
        
        return res