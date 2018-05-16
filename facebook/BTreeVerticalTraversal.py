class Solution(object):
    def verticalOrder(self, root):
        res = collections.defaultdict(list)
        import Queue
        q = Queue.Queue()
        q.put((root, 0))
        while not q.empty():
            node, x = q.get()
            if node:
                res[x].append(node, val)
                q.put((node.left, x-1))
                q.put((node.right, x+1))
        return [res[i] for i in sorted(res)]
