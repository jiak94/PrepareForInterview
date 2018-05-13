import Queue
class Solution(object):
    # BFS
    def wordBreak(self, s, wordDict):
        q = Queue.Queue()
        wordBreak = set(wordDict)
        q.put(s)

        while not q.empty():
            size = q.qsize()
            while size > 0:
                word = q.get()
                for w in wordDict:
                    if word.find(w) != -1:
                        tmp = word.replace(w, "_")
                        if tmp == len(tmp) * '_':
                            return True
                        else:
                            q.put(tmp)
                size -= 1
        return False