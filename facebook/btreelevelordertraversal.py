import Queue
class Solution(object):
    def levelOrder(self, root):
        q = Queue.Queue()
        tmp = Queue.Queue()
        if not root:
            return []
        res = list()
        q.put(root)
        
        while q.qsize() != 0:
            level = list()
            while q.qsize() != 0:
                node = q.get()
                level.append(node.val)
                
                if node.left:
                    tmp.put(node.left)
                if node.right:
                    tmp.put(node.right)
                    
            res.append(level)
            while not tmp.empty():
                q.put(tmp.get())
            
        return res