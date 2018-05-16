class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        import Queue
        hashtable = dict()

        q = Queue.Queue()
        q.put(node)
        p1 = node
        p2 = UndirectedGraphNode(node.val)

        hashtable[node] = p2

        while not q.empty():
            p1 = q.get()
            p2 = hashtable[p1]
            for i in range(len(p1.neighbors)):
                new_node = UndirectedGraphNode(p1.neighbors[i])
                if new_node in hashtable:
                    p2.neighbors.append(new_node)
                else:
                    tmp = UndirectedGraphNode(new_node.val)
                    p2.neighbors.append(tmp)
                    hashtable[new_node] = tmp
                    q.put(new_node)
                    
        return hashtable[node]